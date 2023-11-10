import re

def has_chinese_character(line):
    """检查字符串中是否有中文字符"""
    return re.search(r'[\u4e00-\u9fa5]', line)

def is_valid_paragraph(para):
    """检查段落是否符合给定条件"""
    lines = para.split('\n')
    if not all(has_chinese_character(line) for line in lines):
        return False
    if len(lines) <= 3 or len(lines) % 2 == 1:
        return False
    if '原文' in para or '译文' in para:
        return False
    return True

def read_paragraphs(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        paragraphs = content.split('\n\n')
    return paragraphs

def save_paragraphs(paragraphs, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        for para in paragraphs:
            f.write(para)
            f.write("\n\n")

input_file = '/opt/caregpt/text_tool/主动学习/chat_chinese_test.txt'
output_file = '/opt/caregpt/text_tool/主动学习/chat_chinese_cleaned.txt'
paragraphs = read_paragraphs(input_file)

# 删除每段的最后一行
paragraphs = ['\n'.join(para.split('\n')[:-1]) for para in paragraphs]

cleaned_paragraphs = [para for para in paragraphs if is_valid_paragraph(para)]
save_paragraphs(cleaned_paragraphs, output_file)
