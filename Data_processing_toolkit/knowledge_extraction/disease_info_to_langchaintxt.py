import json


# 将修改后的字符串保存为 TXT 文件

# 读取并解析 JSON 文件
import json
all_disease=[]#所有疾病

def process_dict(d, f):
    for key, value in d.items():#处理嵌套字典
        if isinstance(value, dict):
            if key in all_disease[1:]:#新的疾病开始
                f.write(f'\n\n\n{key}\n')
                process_dict(value, f)
            elif key in all_disease[0]:#新的疾病开始
                f.write(f'{key}\n')
                process_dict(value, f)
            else:
                f.write(f'{key}:')
                process_dict(value, f)
        else:
            f.write(f'{key}:{value}\n')
        # if key in all_disease:
        #     f.write(f'\n\n')

# 打开并读取JSON文件
with open('./input/disease_info.json', 'r') as json_file:
    data = json.load(json_file)
for key, value in data.items():
    all_disease.append(key)
#所有疾病，但不含第一个
# print(all_disease)
# 打开一个TXT文件以保存输出
with open('./langchain_input/disease_info.txt', 'w') as txt_file:
    process_dict(data, txt_file)


#print(data)
# # 将解析后的 JSON 数据转换回字符串，使用 ensure_ascii=False 来处理非ASCII字符
# json_string = json.dumps(data, ensure_ascii=False)
#
# # 将 { 和 }, 替换为换行
# json_string = json_string.replace("{", "\n").replace("},", "\n")
#
# # 将修改后的字符串保存为 TXT 文件
# with open('./langchain_input/disease_info.txt', 'w', encoding='utf-8') as f:
#     f.write(json_string)
