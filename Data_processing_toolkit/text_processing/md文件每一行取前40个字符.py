file_path = '/opt/caregpt/text_tool/output/老年长期照护与康复指导手册_去目录_去空行.md'
res=''

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        if len(line) > 0:  # 忽略空行
            chinese_chars = line[:10]  # 获取前30个汉字
            #print(chinese_chars)
            #lines.append(chinese_chars)
            res+=chinese_chars
print(len(res))

print(repr(res[1000:2000]))
# print(res[1000:2000])
#print(res[:500])
症治疗目的是控制伴发的精神病理症状