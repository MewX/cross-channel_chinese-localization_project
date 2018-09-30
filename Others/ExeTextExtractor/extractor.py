print('extracting is_r2.exe')

# all test ranges are defined here [inclusive, exclusive]
TEXT_RANGE = [[0xA23B0, 0xA96A4], [0x9EAC0, 0x9F7C8]]

input_file = open("io_r2.exe", "rb")  # strings are encoded in
input_file_content = input_file.read()
input_file.close()
output_file = open("io_r2.exe.txt", 'w', encoding='utf16')

for range_group in TEXT_RANGE:
    start_pos = range_group[0]
    end_pos = range_group[1]

    current_start_pos = start_pos
    while True:
        # skip all empty
        while current_start_pos < end_pos and input_file_content[current_start_pos] == 0:
            current_start_pos = current_start_pos + 1

        # exiting condition
        if current_start_pos >= end_pos:
            break

        # read until empty or end
        current_len = 0
        while current_start_pos + current_len < end_pos and input_file_content[current_start_pos + current_len] != 0:
            current_len = current_len + 1

        # output
        text = input_file_content[current_start_pos: current_start_pos + current_len].replace(b'\x87\x53', b'\x20\x20').decode('shift-jis')
        print(text)
        output_file.write("●0x{:X}+{:d}●{:s}\r\n".format(current_start_pos, current_len, text))
        output_file.write("○0x{:X}+{:d}○{:s}\r\n\r\n".format(current_start_pos, current_len, text))

        # update start pos for next round
        current_start_pos = current_start_pos + current_len

output_file.close()
