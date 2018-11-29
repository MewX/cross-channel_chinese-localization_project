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
    lines = src.readlines()
    old_txt_lines = old_txt_file.readlines()
    source_lines = source.readlines()

    # loop through the source and get all source texts
    source_text_parsed = list()
    speaker_name = ""
    expecting = 0
    for i in range(1, len(source_lines) - 1):
        line = source_lines[i].strip()
        if len(line) == 0:
            continue  # ignore all empty lines

        if re.match(r'^<\d\d.+?single>$', line):
            # begin of a section
            assert expecting is 0 or expecting is 1  # sometimes the single block is empty
            expecting = 1
        elif re.match(r'^<\d\d.+?double>$', line):
            # begin of a section
            assert expecting is 0  # having issues with ED02 from source!!!!
            speaker_name = ""
            expecting = 2
        elif expecting == 2:
            speaker_name = line
            expecting -= 1
        else:
            output_text = line
            if speaker_name != "":
                output_text = '[{}]{}'.format(speaker_name, line)
            print("src: " + output_text)
            source_text_parsed.append(output_text)
            expecting -= 1

    # new text
    new_txt_result = list()
    new_txt_translated = list()
    speaker_name = ""
    in_section = False
    passed_source_text = False
    for i in range(1, len(lines) - 1):
        line = lines[i].strip()
        # print("'{}' LINE {}: {}".format(filename, i + 1, line))
        if len(line) == 0:
            continue  # ignore all empty lines

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
                    # a set of annoying replacements are listed here
                    source_text = source_text.replace("—", "ー")  # dash
                    if source_text[0] == "“" and source_text[-1] == "”":
                        source_text = "「" + source_text[1:-1] + "」"

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
                # a set of annoying replacements are listed here
                # source_text = translated_text.replace("—", "ー")  # dash

                # generate the output_text
                output_text = '[{}]{}'.format(speaker_name, translated_text)
            new_txt_translated.append(output_text)
            print("trans: " + output_text)

            in_section = False
            passed_source_text = False
            speaker_name = ""
        else:
            assert False

    # comparing the result text and old_txt
    print("'{}' comparing ----------------------------------------".format(filename))
    i_old_txt = 0
    for i in range(len(new_txt_result) - 1):
        output_text = new_txt_result[i]
        old_text = old_txt_lines[i_old_txt].strip()

        if output_text != old_text:
            # try to search down in old_txt_lines first
            diff = 1
            while i_old_txt + diff < len(old_txt_lines) and output_text != old_txt_lines[i_old_txt + diff].strip():
                diff += 1
            if i_old_txt + diff < len(old_txt_lines):
                # found it! then damn-it text has one line missing
                for i_diff in range(0, diff - 1):
                    print("'{}' ERROR: damn-it text missing one line O#{}: '{}'"
                          .format(filename, i_old_txt + 1, old_txt_lines[i_old_txt + i_diff].strip()))
                i_old_txt += diff
            else:
                # not found, then old text has one line missing
                print("'{}' ERROR: my text missing one line D#{}: '{}'"
                      .format(filename, i, output_text))
                i_old_txt -= 1
        else:
            # good, matching
            print("'{}' GOOD: matching D#{}: '{}'".format(filename, i, output_text))
            pass

        # prepare for the next damn-it text
        i_old_txt += 1

    # then output the damn-it text missing endings
    while i_old_txt < len(old_txt_lines):
        print("'{}' ERROR: damn-it text missing one line O#{}: '{}'"
              .format(filename, i_old_txt + 1, old_txt_lines[i_old_txt].strip()))
        i_old_txt += 1

    print("'{}' ending ----------------------------------------\n".format(filename))
