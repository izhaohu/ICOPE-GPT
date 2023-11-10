
markdown_file_path = '/opt/caregpt/text_tool/output/老年长期照护与康复指导手册acrobat.md'  # 替换为实际的Markdown文件路径



import re

def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    pattern = r'^(#+)\s*(.*?)\s*$(.*?)^(?=^#+|\Z)'
    matches = re.findall(pattern, content, flags=re.MULTILINE | re.DOTALL)

    result = []
    for match in matches:
        title_level = len(match[0])  # 获取标题级别，即#的数量
        title = match[1].strip()  # 去除标题两端的空格
        content = match[2].strip()  # 去除内容两端的空格
        result.append((title_level, title, content))

    return result

# 读取Markdown文件，并将标题、级别和内容保存到列表

markdown_list = read_markdown_file(markdown_file_path)

# 打印标题、级别和内容
for title_level, title, content in markdown_list:
    print(f'Level: {"#" * title_level}')
    print(f'Title: {title}')
    print(f'Content: {content}')
    print('---')
