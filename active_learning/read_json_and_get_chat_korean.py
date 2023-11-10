import json

# 读取文件
file_path = "/opt/caregpt/text_tool/主动学习/carecall_filtered_10k.json"
# 写入文件
out_path1 = "/opt/caregpt/text_tool/主动学习/chat_korean.txt"
# out_path2 = "/opt/caregpt/text_tool/主动学习/chat_korean2.txt"

with open(out_path1, 'a', encoding='utf-8') as file1:
# 读取并加载JSON文件
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for id,i in enumerate(data):
            #if id <=2000:
            for j in i["data"]:
                file1.write(j["text"])
                file1.write("\n")
            file1.write("\n")

# with open(out_path2, 'a', encoding='utf-8') as file2:
# # 读取并加载JSON文件
#     with open(file_path, 'r', encoding='utf-8') as f:
#         data = json.load(f)
#         for id,i in enumerate(data):
#             if id >5000:
#                 continue
#             for j in i["data"]:
#                 file2.write(j["text"])
#                 file2.write("\n")
#             file2.write("\n")



# 打印加载的数据（你可以根据需求进行修改）
#print(len(data))#10500

# 如果需要对数据进行进一步处理，可以在此添加代码
