import re
import os
markdown_file_path='/opt/caregpt/text_tool/output/老年长期照护与康复指导手册 - 缪荣明 -.md'


def read_markdown_file(file_path):
    full_file_name = os.path.basename(file_path)  # 获取完整文件名
    file_name, file_ext = os.path.splitext(full_file_name)  # 分离文件名和后缀

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    pattern = r'^(#+)\s*(.*?)\s*$(.*?)^(?=^#+|\Z)'
    matches = re.findall(pattern, content, flags=re.MULTILINE | re.DOTALL)

    result = []
    parent_titles = ["" ] * 10
    same_level_titles = [ [] for _ in range(10) ]
    all_titles_at_same_level = [ [] for _ in range(10) ]  # 新增，用于保存同一层级的所有标题
    last_parent_title = [None] * 10
    title_hierarchy = [0] * 10
    title_count = 0

    for match in matches:
        title_level = len(match[0])
        title = match[1].strip()
        content = match[2].strip()

        current_parent_title = (
            parent_titles[title_level - 2] if title_level > 1 else None
        )

        if current_parent_title != last_parent_title[title_level - 1]:
            same_level_titles[title_level - 1] = []
            all_titles_at_same_level[title_level - 1] = []  # 当进入新的父标题时，清空当前级别的所有标题
            last_parent_title[title_level - 1] = current_parent_title
            title_hierarchy[title_level - 1] = 0

        title_hierarchy[title_level - 1] += 1

        parent_titles[title_level - 1] = title
        same_level_titles[title_level - 1].append(title)
        all_titles_at_same_level[title_level - 1].append(title)  # 将当前标题添加到同一层级的所有标题列表中

        parent_title_str = " > ".join(
            filter(None, [parent_titles[i] for i in range(title_level)])
        )

        same_level_title_str = ", ".join(same_level_titles[title_level - 1])

        title_hierarchy_str = "-".join(map(str, title_hierarchy[:title_level]))

        title_count += 1
        title_id = f'{file_name}_{title_count}{file_ext}'

        # 获取同一层级的所有标题，以 ", " 分隔
        all_titles_at_same_level_str = ", ".join(all_titles_at_same_level[title_level - 1])

        result.append(
            (title_level, title, content, parent_title_str, same_level_title_str, full_file_name, title_hierarchy_str, title_id, all_titles_at_same_level_str)
        )

    return result


markdown_list = read_markdown_file(markdown_file_path)

for title_level, title, content, parent_titles, same_level_titles, file_name, title_hierarchy, title_id ,all_titles_at_same_level_str in markdown_list:
    print(f'Level: {"#" * title_level}')
    print(f'Title: {title}')
    print(f'Content: {content}')
    print(f'Parent Titles: {parent_titles}')
    print(f'Same Level Titles: {same_level_titles}')
    print(f'File Name: {file_name}')
    print(f'Title Hierarchy: {title_hierarchy}')
    print(f'Title ID: {title_id}')
    print(f'all_titles_at_same_level_str: {all_titles_at_same_level_str}')
