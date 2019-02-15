import re
import sys
import os

# TODO: List
"""
1. need to support %K%p
2. TXT choices are not shown
3. close %K%P are not extracted, e.g. ED02.WSC: 遍在する未来？新たに見出された過去？
"""

print(repr(sys.argv))

if len(sys.argv) != 5:
    # py convertio.py
    # /dev/shm/rio_workspace/damnit_txt
    # /dev/shm/rio_workspace/new_txt
    # /dev/shm/rio_workspace/old_txt
    # /dev/shm/rio_workspace/source
    print("usage: python xxx.py <old_txt_folder_path> <new_txt_folder_path> <old_txt_folder_path> <original_damn_txt>")
    sys.exit()


NOT_MATCHING_CHAR = ("ー", "―", "—", "‘", "’", "“", "”", "「", "」", "《", "》", "『", "』")
NOT_INCLUDED_CHAR = ("！", "。", "　")


def rip(text):
    # replace all not matching characters
    for c in NOT_MATCHING_CHAR:
        text = text.replace(c, 'x')

    # remove all excluded char
    for c in NOT_INCLUDED_CHAR:
        text = text.replace(c, '')
    return text


def walk(adr):
    mylist = []
    for root, dirs, files in os.walk(adr):
        for name in files:
            adrlist = os.path.join(root, name)
            mylist.append(adrlist)
    return mylist


dst_path = sys.argv[2]
if dst_path[-1] != '/':
    dst_path = dst_path + '/'  # adding trailing '/'

old_txt_path = sys.argv[3]
if old_txt_path[-1] != '/':
    old_txt_path = old_txt_path + '/'  # adding trailing '/'

original_path = sys.argv[4]
if original_path[-1] != '/':
    original_path = original_path + '/'  # adding trailing '/'

fl = walk(sys.argv[1])[:3]  # todo: disable this
for fn in fl:
    if 'txt' not in fn.lower():
        print('error in filename: ' + fn)
        continue

    filename = fn[fn.rindex('/') + 1:]
    old_txt_filename = old_txt_path + filename
    dstname = dst_path + filename
    source_name = original_path + filename
    print("from {} to {}".format(fn, dstname))
    src = open(fn, 'r', encoding='utf16')
    old_txt_file = open(old_txt_filename, 'r', encoding='shift_jis')
    dst = open(dstname, 'w', encoding='utf16')
    source = open(source_name, 'r', encoding='utf16')

    # main logic
    print("'{}' begin ----------------------------------------".format(filename))
    lines = src.readlines()                   # translated damn-it text
    old_txt_lines = old_txt_file.readlines()  # my txt file
    source_lines = source.readlines()         # untranslated damn-it text file

    # loop through the source and get all source texts
    source_text_parsed = list()
    speaker_name = ""
    expecting = 0
    for i in range(len(source_lines) - 1):
        line = source_lines[i].strip()
        if len(line) == 0 or i == 0 and re.match(r'^<!.*?', line):
            continue  # ignore all empty lines

        if re.match(r'^<\d\d.+?single>$', line):
            # begin of a section
            assert expecting is not 2  # sometimes the single block is empty
            expecting = 1
        elif re.match(r'^<\d\d.+?double>$', line):
            # begin of a section
            assert expecting is not 2  # sometimes the single block is empty and followed by a double block
            speaker_name = ""
            expecting = 2
        elif expecting == 2:
            speaker_name = line
            expecting -= 1
        else:
            output_text = line
            if speaker_name != "":
                output_text = '[{}]{}'.format(speaker_name, line)
            # print("src: " + output_text)
            source_text_parsed.append(output_text)
            expecting -= 1

    # new text
    new_txt_result = list()
    new_txt_translated = list()
    speaker_name = ""
    in_section = False
    passed_source_text = False
    for i in range(len(lines) - 1):
        line = lines[i].strip()
        # print("'{}' LINE {}: {}".format(filename, i + 1, line))
        if len(line) == 0 or i == 0 and re.match(r'^<!.*?', line):
            continue  # ignore all empty lines

        line = rip(line)
        if re.match(r'^<\d\d.+?$', line):
            # begin of a section
            assert in_section is False
            assert passed_source_text is False
            in_section = True
        elif re.match(r'^<!.*?', line):
            # source text
            assert in_section is True
            passed_source_text = True
            matcher = re.match(r'^<!(.*?)>$', line)
            if matcher:
                source_text = matcher.group(1).strip()
                if len(source_text) == 0:
                    in_section = False
                    passed_source_text = False
                    continue

                output_text = source_text
                if len(speaker_name) != 0:
                    # generate the output_text
                    output_text = '[{}]{}'.format(speaker_name, source_text)
                new_txt_result.append(output_text)
                # print(output_text)
            else:
                print("ERROR: not found full tag")
                sys.exit(-1)
        elif in_section and not passed_source_text:
            # the name section
            speaker_name = line
        elif in_section and passed_source_text:
            # the main translated text section
            translated_text = line
            output_text = translated_text

            if len(speaker_name) != 0:
                # generate the output_text
                output_text = '[{}]{}'.format(speaker_name, translated_text)
            new_txt_translated.append(output_text)
            # print("trans: " + output_text)

            in_section = False
            passed_source_text = False
            speaker_name = ""
        else:
            assert False

    # comparing the result text and old_txt
    print("'{}' comparing ----------------------------------------".format(filename))
    final_translated_txt = []
    i_old_txt = 0
    for i in range(len(new_txt_result)):
        output_text = new_txt_result[i]  # already ripped
        old_text = old_txt_lines[i_old_txt].strip() if i_old_txt < len(old_txt_lines) else None  # could be shorter

        # replace all not matching characters
        if old_text is not None:
            old_text = rip(old_text)

        if output_text != old_text:
            print("'{}' ERROR: HIGH LEVEL NOT MATCHING: '{}' - '{}'".format(filename, output_text, old_text))

            # try to search down in old_txt_lines first
            diff = 1
            while i_old_txt + diff < len(old_txt_lines) and output_text != rip(old_txt_lines[i_old_txt + diff].strip()):
                diff += 1
            if i_old_txt + diff < len(old_txt_lines):
                # found it! then damn-it text has one line missing
                for i_diff in range(diff):
                    missing_line = old_txt_lines[i_old_txt + i_diff].strip()
                    print("'{}' ERROR: damn-it missing one line O#{}: '{}'"
                          .format(filename, i_old_txt + 1, missing_line))
                    final_translated_txt.append(missing_line)
                i_old_txt += diff  # fixme: bug here
            else:
                # not found, then old text has one line missing
                print("'{}' ERROR: my text missing one line D#{}: '{}' - '{}'"
                      .format(filename, i,
                              old_txt_lines[i_old_txt].strip() if i_old_txt < len(old_txt_lines) else None,
                              new_txt_translated[i]))
                i_old_txt -= 1
        else:
            # good, matching
            new_txt_result[i] = old_txt_lines[i_old_txt].strip()
            print("'{}' GOOD: matching D#{}: '{}'".format(filename, i, new_txt_result[i]))
            final_translated_txt.append(new_txt_translated[i])
            pass

        # prepare for the next damn-it text
        i_old_txt += 1

    # then output the damn-it text missing endings
    while i_old_txt < len(old_txt_lines):
        missing_line = old_txt_lines[i_old_txt].strip()
        print("'{}' ERROR: damn-it text missing one line O#{}: '{}'"
              .format(filename, i_old_txt + 1, missing_line))
        final_translated_txt.append(missing_line)
        i_old_txt += 1

    print("'{}' ending ----------------------------------------\n".format(filename))

    print("old txt line: {} VS final translated txt {}".format(len(old_txt_lines), len(final_translated_txt)))
    assert len(old_txt_lines) == len(final_translated_txt)
    for txt in final_translated_txt:
        print("translate to: '{}'".format(txt))
