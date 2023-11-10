import json

# 输入文件路径
input_file_path = "/opt/caregpt/text_tool/merged_output_ad.json"
# 输出文件路径
output_file_path = input_file_path.rsplit('.', 1)[0] + '.jsonl'

# 从文件中读取JSON数据
with open(input_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 将数据转换为JSONL格式并写入新的文件
with open(output_file_path, 'w', encoding='utf-8') as f:
    for item in data:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
