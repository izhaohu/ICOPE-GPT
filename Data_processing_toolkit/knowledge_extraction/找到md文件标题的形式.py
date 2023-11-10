file_path = '/opt/caregpt/text_tool/output/老年长期照护与康复指导手册acrobat.md'
lines = []

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()  # 去除行首尾的空白字符
        if len(line) > 0:  # 忽略空行
            chinese_chars = line[:30]  # 获取前30个汉字
            lines.append(chinese_chars)

print(len(lines))
print(lines[:1000])

