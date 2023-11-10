import re
input_file = '/opt/caregpt/text_tool/主动学习/chat_chinese_cleaned.txt'
output_file = '/opt/caregpt/text_tool/主动学习/goodchat_by_chatgpt.txt'

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


paragraphs = read_paragraphs(input_file)

#
for para in paragraphs:
    #print(para)
    #读取一行
    lines = para.split('\n')
    1/0

#save_paragraphs(cleaned_paragraphs, output_file)
