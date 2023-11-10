import json

# 输入和输出文件路径
input_file_path = "/opt/caregpt/text_tool/input/GenMedGLM-8k.json"
output_file_path = "/opt/caregpt/text_tool/output_json/moshadong-8k.json"
#GenMedGLM-8k.json
#GenMedGPT-5k-ch.json
# 从文件中读取JSON数据
with open(input_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 遍历列表中的每个字典，删除 "instruction" 键，并将 "input" 改为 "question"，"output" 改为 "answer"
for item in data:
    if "instruction" in item:
        del item["instruction"]
    if "input" in item:
        item["question"] = item.pop("input")
    if "output" in item:
        item["answer"] = item.pop("output")

# 将处理后的数据写入新的文件
with open(output_file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)