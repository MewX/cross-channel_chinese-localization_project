import re
import sys
import os

print(repr(sys.argv))

if len(sys.argv) != 3:
    # python convertio.py /dev/shm/rio_workspace/damnit_txt /dev/shm/rio_workspace/new_txt
    print("usage: python xxx.py <old_txt_folder_path> <new_txt_folder_path>")
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
fl = walk(sys.argv[1])[:3]  # todo: disable this
for fn in fl:
    if 'txt' not in fn.lower():
        print('error in filename: ' + fn)
        continue

    filename = fn[fn.rindex('/') + 1:]
    dstname = dst_path + filename
    print("from {} to {}".format(fn, dstname))
    src = open(fn, 'r', encoding='utf16')
    dst = open(dstname, 'w', encoding='utf16')

    # main logic
    lines = src.readlines()
    speaker_name = ""
    in_section = False
    passed_source_text = False
    for i in range(1, len(lines) - 1):
        line = lines[i].strip()
        print("'{}' LINE {}: {}".format(filename, i + 1, line))
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
                if len(speaker_name) == 0:
                    print(source_text)
                else:
                    print('[{}]{}'.format(speaker_name, source_text))
            else:
                print("ERROR: not found full tag")
                sys.exit(-1)
        elif in_section and not passed_source_text:
            # the name section
            speaker_name = line
        elif in_section and passed_source_text:
            # the main translated text section
            translated_text = line
            in_section = False
            passed_source_text = False
        else:
            assert False
