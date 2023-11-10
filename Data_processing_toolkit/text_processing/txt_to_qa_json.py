import json
#霍普金斯护理循证实践模型与指南
#霍普金斯实施与转化
############老年长期照护与康复指导手册
#######老年医学_1-450_ocr
#########老年医学_451-900_ocr
#########老年医学_901-127
##############中国痴呆与认知障碍诊治指南书籍_ocr.pdf
#################老年住宅_ocr.pdf
################居家适老改造手帐_ocr.pdf
#################血管通电子书_ocr.pdf
##################卫生部_老年人跌倒_ocr.pdf
################老年人跌倒干预技术指南_ocr.pdf
# 防跌倒坠床预案及处理流程.pdf
# 高龄老人跌倒原因及预防对策.pdf
# 容易跌倒的理由及预防方法.pdf
# #####################长者跌倒干预技术指南2023.pdf
# 长者跌倒预防风险评估及预防.pdf
# WHO_预防和管理整个生命过程中跌倒的策略.pdf
import os

def count_sep(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    return content.count('[sep]')

def process_file(file_name,output_dir,output_file_name):
    data = []
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        # 跳过空行
        if line.strip() == '':
            i += 1
            continue
        # 跳过没有问号的行
        if ('?' not in line) and ('？' not in line):
            i += 1
            continue
        # 如果满足条件，将该行作为问题
        #print(line)
        if line.startswith("问题：") or line.startswith("问：") or line.startswith("Question:") or line.startswith("问题: ") or\
                line.startswith("\n问题：") or line.startswith("\n问：") or line.startswith("\nQuestion:"):
            question = line.replace("问题：", "", 1).replace("问题： ", "", 1).replace("问：", "", 1).replace("Question:", "", 1)\
                .replace("\n问题：", "", 1).replace("\n问：", "", 1).replace("\nQuestion:", "", 1)
        answer = ''
        i += 1
        # 合并接下来的行作为答案，直到遇到[sep]或者“参考文献”
        while i < len(lines) and '[sep]' not in lines[i]:
            if '参考文献' in lines[i]:
                break
            if '不适合生成' in lines[i]:
                break
            if '以上答案长度' in lines[i]:
                break
            if '总长度' in lines[i]:
                break
            if '生成的问答对' in lines[i]:
                break
            if '基于所给的文本，以上是' in lines[i]:
                break
            if '参考文本：' in lines[i]:
                break
            if '参考答案长度' in lines[i]:
                break
            if '适合小学生理解' in lines[i]:
                break
            if '小学生也能理解' in lines[i]:
                break
            if '参考资料' in lines[i]:
                break
            if '简化版回答' in lines[i]:
                break
            if '参考资料' in lines[i]:
                break
            if '无法生成' in lines[i]:
                break
            if '很抱歉' in lines[i]:
                break
            if '参考资料' in lines[i]:
                break
            if lines[i].startswith("答案：") or lines[i].startswith("答：") or lines[i].startswith("Answer:") or lines[i].startswith("答案：")\
                    or lines[i].startswith("\\n答案：") or lines[i].startswith("\\n答：") or lines[i].startswith("\\nAnswer:") :
                lines[i] = lines[i].replace("答案：", "", 1).replace("答案： ", "", 1).replace("答：", "", 1).replace("Answer:", "", 1)\
                    .replace("\\n答案：", "", 1).replace("\\n答：", "", 1).replace("\\nAnswer:", "", 1)
            #print(line)

            answer += lines[i]
            i += 1
        # print(question)
        # print(answer)
        if question and answer:
            data.append({"question": question, "answer": answer})
        i += 1
    # 将数据保存为json文件

    # 将数据保存为json文件
    with open(os.path.join(output_dir, output_file_name+'.json'), 'w', encoding='utf-8') as json_f:
        json.dump(data, json_f, ensure_ascii=False)
    global count_data
    count_data=len(data)


if __name__ == "__main__":
    # 调用函数处理文本文件
    dir = "/opt/caregpt/text_tool/output/AD相关知识库"
    for file in os.listdir(dir):
        print(os.path.join(dir, file))
        if os.path.isfile(os.path.join(dir, file)):
            file_name=os.path.join(dir, file)
            output_dir = "/opt/caregpt/text_tool/output_json/AD相关知识库"
            # 如果输出文件夹不存在，则创建它
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            output_file_name = file_name.split(".")[0].split("/")[-1]
            process_file(file_name,output_dir,output_file_name)
            print('处理前文本中的问答对个数：'+str(count_sep(file_name)))
            print('处理后文本中的问答对个数：'+str(count_data))
