
markdown_file_path = '/opt/caregpt/text_tool/output/老年长期照护与康复指导手册acrobat.md'  # 替换为实际的Markdown文件路径

import markdown

def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    md = markdown.Markdown(extensions=['markdown.extensions.toc'])
    html = md.convert(content)
    toc = md.toc

    result = {}
    current_title = ''
    for line in html.split('\n'):
        if line.startswith('<h'):
            title_level = int(line[2])  # 提取标题级别
            current_title = line[line.find('>') + 1:line.rfind('<')].strip()  # 提取标题内容
        elif line.startswith('<p>') and current_title:
            content = line[3:line.rfind('</p>')].strip()  # 提取内容
            result[current_title] = (title_level, content)

    return result

# 读取Markdown文件，并将标题、级别和内容保存到字典
#markdown_file_path = 'example.md'  # 替换为实际的Markdown文件路径
markdown_dict = read_markdown_file(markdown_file_path)

# 打印字典内容
for title, (level, content) in markdown_dict.items():
    print(f'Level: {"#" * level}')
    print(f'Title: {title}')
    print(f'Content: {content}')
    print('---')
