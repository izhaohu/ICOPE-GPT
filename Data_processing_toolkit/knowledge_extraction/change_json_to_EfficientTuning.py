import json

# 载入原始文件
with open('/opt/caregpt/text_tool/merged_output_slhgz.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 修改键值
for item in data:
    item['instruction'] = item.pop('question')
    item['output'] = item.pop('answer')
    item['input'] = ''

# 输出到新文件
with open('/opt/caregpt/text_tool/merged_output_slhgz_eff.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
