from itertools import zip_longest
from pathlib import Path

'''
get_all_rpy_file(folder: Path) -> set
获取 folder 路径下所有的 rpy 文件，返回一个 set
'''
def get_all_rpy_file(folder: Path) -> set:
    ret_set = set()
    for p in folder.rglob('*'):
        rp = p.relative_to(folder)
        pstr = str(rp)
        if pstr.endswith(".rpy"):
            ret_set.add(rp)
    return ret_set


'''
compare_folder_tree(dir1:str, dir2:str) -> bool
比较 dir1 和 dir2 目录树的差异，此项目中仅比较 rpy 文件的差异，相同返回 True，否则返回 False
'''
def compare_folder_tree(dir1:str, dir2:str) -> bool:
    dir1 = Path(dir1)
    dir2 = Path(dir2)
    tree1 = get_all_rpy_file(dir1)
    tree2 = get_all_rpy_file(dir2)

    only_in_1 = tree1 - tree2
    only_in_2 = tree2 - tree1
    common = tree1 & tree2

    if len(only_in_1) or len(only_in_2):
        print(f"仅在 {dir1} 中存在的项目：")
        for p in sorted(only_in_1):
            print(f"  {p}")
        print(f"仅在 {dir2} 中存在的项目：")
        for p in sorted(only_in_2):
            print(f"  {p}")
        print(f"共同项目：{len(common)} 个")
        return False
    return True

'''
get_all_lines_start_with(line_str:str, file_path:str) -> list
获取 file_path 对应的文件，其以 line_str 开头的所有内容行，返回一个 list
'''
def get_all_lines_start_with(line_str:str, file_path:str) -> list:
    result = list()
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith(line_str):
                # 去掉末尾换行符，保留行内容
                result.append(line.rstrip('\n'))
    return result

'''
compare_file_block(left: str, right: str) -> bool
该函数比较 left 路径和 right 路径对应 rpy 文件内的翻译块是否相同，相同返回 True，否则返回 False。
主要比较以下几个方面：
1. 以 'translate simplified_chinese ' 开头的内容行数量是否相同
2. 'translate simplified_chinese strings:' 行所在的位置是否相同。Ren'Py 生成的文件，会统一把所有游戏选项放在该行下方，例如：

translate simplified_chinese strings:

    # game/scripts/cca/cca0004.rpy:236
    old "どうしよう。"
    new "怎么办？"
    # game/scripts/cca/cca0004.rpy:236
    old "屋上に行く"
    new "去天台"
    # game/scripts/cca/cca0004.rpy:236
    old "冬子と話す"
    new "和冬子说话"

原字幕组文件中，每个选项都分开放在了对话之间，若不将位置统一，则本方法下更新后的 hash 会错位。
3. '    # game/scripts/xxx/xxxx.rpy:xxx' 是否一致，该文件是游戏内日文原文路径，Ren'Py 生成的翻译框架内，
每一个翻译都注释了其对应到原文的位置，原字幕组文件中也是如此。但我在翻译中发现原字幕组文件中存在多个相同位置的留空
翻译，虽然不影响游戏正常运行，但是如果不去掉，会影响本方法更新 hash 值的正确性
'''
def compare_file_block(left: str, right: str) -> bool:
    left_file_translate_lines = get_all_lines_start_with("translate simplified_chinese", left)
    right_file_translate_lines = get_all_lines_start_with("translate simplified_chinese", right)

    if len(left_file_translate_lines) != len(right_file_translate_lines):
        print(f"文件 <{left}> 和文件 <{right}> 存在不同的翻译块，请检查！")
        return False

    for i in range(len(left_file_translate_lines)):
        if left_file_translate_lines[i] == "translate simplified_chinese strings:" and right_file_translate_lines[i] != left_file_translate_lines[i]:
            print(f"文件 <{left}> 和文件 <{right}> 存在不同的选项翻译行，请检查！ ")
            return False

    left_file_line_list = get_all_lines_start_with("    # \"", left)
    right_file_line_list = get_all_lines_start_with("    # \"", right)

    if not left_file_line_list == right_file_line_list:
        print(f"文件 <{left}> 和文件 <{right}> 存在不同的原文对应行，请检查！")
        # 用 zip_longest 填充，默认 fillvalue 为 None
        # 为了显示 "empty"，我们将 None 替换为字符串 "empty"
        fill = "empty"
        for idx, (a, b) in enumerate(zip_longest(left_file_line_list, right_file_line_list, fillvalue=fill)):
            a_str = str(a) if a != fill else fill
            b_str = str(b) if b != fill else fill
            print(f"文件 <{left}> 和文件 <{right}> 在第 {idx} 个文件对应行存在差异： {a_str} 和 {b_str} 不一致")

            return False

    return True

'''
find_lines_starting_with_prefix(file_path:str, prefix:str) -> list:
    返回文件中所有以指定前缀开头的行及其行号（从1开始）。
    返回列表，元素为 (行号, 行内容) 元组。
'''
def find_lines_starting_with_prefix(file_path:str, prefix:str) -> list:
    results = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_no, line in enumerate(f, start=1):
                if line.startswith(prefix):
                    results.append((line_no, line.rstrip('\n')))
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 不存在。")
    except Exception as e:
        print(f"读取文件时出错：{e}")
    return results

'''
replace_single_line(file_path:str, line_number:int, new_content:str)
将路径为 file_path 文件内的行号 line_number 行号对应的行内容替换为 new_content
'''
def replace_single_line(file_path:str, line_number:int, new_content:str):
    print(f"开始替换文件 {file_path} 第 {line_number} 行为 {new_content}")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 不存在。")
        return

    total = len(lines)

    # 行号合法性检查
    if line_number < 1:
        print("错误：行号必须 >= 1")
        return
    if line_number > total:
        print(f"错误：文件只有 {total} 行，无法替换第 {line_number} 行。")
        return

    # 替换指定行（保留原行的换行符风格，或统一用 '\n'）
    lines[line_number - 1] = new_content + '\n'

    # 写回文件
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"已替换第 {line_number} 行为：{new_content}")
    except Exception as e:
        print(f"写文件出错：{e}")

'''
update_block_hash(aim:str, source:str) -> bool
从 source 路径对应的文件中，同步翻译块的 hash 值到 aim 路径对应的文件，具体步骤如下：
1. 获取 source 对应文件中的所有 "translate simplified_chinese" 开头的行
2. 获取 aim 对应文件中，所有 "translate simplified_chinese" 开头的行 content，以及对应的行号 num，组成 list<(num, content)>
3. 检查长度是否一致，不一致则放弃更新
4. 将 aim 文件中 num 行对应内容替换为 source 中的对应行
'''
def update_block_hash(aim:str, source:str) -> bool:
    source_file_translate_lines = get_all_lines_start_with("translate simplified_chinese", source)
    aim_file_translate_lines_with_num = find_lines_starting_with_prefix(aim, "translate simplified_chinese")
    if len( source_file_translate_lines ) != len(aim_file_translate_lines_with_num):
        print(f"文件 <{aim}> 和文件 <{source}> 翻译行数量不一致，请检查")
        return False
    for i in range(len(source_file_translate_lines)):
        num, content = aim_file_translate_lines_with_num[i]
        replace_single_line(aim, num, source_file_translate_lines[i])
    return True

def main():
    # 原先带有字幕组翻译的 tl 文件夹命名为 `tl_bak`
    # 由于 Ren‘Py 生成的翻译框架命名为 `tl`
    tl_content_folder = "./tl_bak"
    tl_framework_folder = "./tl"

    if not compare_folder_tree(tl_content_folder, tl_framework_folder):
        print(f"字幕组翻译文件夹目录树 <{tl_content_folder}> 与 Ren'Py 生成的翻译文件夹目录树 <{tl_framework_folder}> 不一致，请检查！")
        exit(1)

    tl_content_rpy_files = get_all_rpy_file(Path(tl_content_folder))
    tl_framework_rpy_files = get_all_rpy_file(Path(tl_framework_folder))

    tl_c_list = list(tl_content_rpy_files)
    tl_f_list = list(tl_framework_rpy_files)

    if len(tl_c_list) != len(tl_f_list):
        print(f"字幕组翻译文件夹内 rpy 文件的数量 <{len(tl_c_list)}> 与 Ren'Py 生成的翻译文件夹内 rpy 文件的数量 <{len(tl_f_list)}> 不一致，请检查！")
        exit(1)

    compare_same = True
    for i in range(len(tl_c_list)):
        tlcf = tl_content_folder + "/" + str(tl_c_list[i])
        tlff = tl_framework_folder + "/" + str(tl_f_list[i])

        if not compare_file_block(tlcf, tlff):
            print(f"字幕组翻译文件 <{str(tlcf)}> 与 Ren'Py 生成文件 <{str(tlff)}> 的翻译块存在差异，请检查！")
            compare_same = False
    if not compare_same:
        exit(1)

    for i in range(len(tl_c_list)):
        tlcf = tl_content_folder + "/" + str(tl_c_list[i])
        tlff = tl_framework_folder + "/" + str(tl_f_list[i])
        # update_block_hash(a, b) 将 b 中的翻译快 hash 值同步到 a
        update_block_hash(tlcf, tlff)

if __name__ == "__main__":
    main()


