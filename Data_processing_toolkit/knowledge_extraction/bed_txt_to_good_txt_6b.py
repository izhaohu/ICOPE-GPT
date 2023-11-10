from chat_with_chatgpt import chat_with_chatpgt
from chat_with_6b import chat_with_6b
from prompt_file.prompt_file import prompt_template
import time
from datetime import datetime
# link=r"./老年长期照护与康复指导手册 - 缪荣明.pdf.txt"
# print(link)
link="/opt/caregpt/text_tool/老年长期照护与康复指导手册 - 缪荣明.pdf.txt"

#计算需要睡眠的时间
def sleep_time(a,b):
    diff = b - a
    runtime=diff.total_seconds()
    #print(runtime)
    if runtime>20:
        pass
    else:
        time.sleep(21-runtime)

#这本书一共有多少页
def count_numpage(file_path,chars_per_page):
    with open(link, 'r',encoding='utf-8') as file:
        #print(repr(file.read()))
        num_page=0
        while file.read(600):
            num_page+=1
    return num_page
    file.close()
print(count_numpage(link,600))#139

#去除多余空格 语法错误
with open(link, 'r',encoding='utf-8') as file:
    #print(repr(file.read()))
    count=0
    previous=""
    while True:
        count+=1
        #content = repr(file.read(1000))
        content = file.read(600)
        # next = previous_next[100:]
        # content=previous_next[:100]

        if count <2:
            prompt = prompt_template("grammar",content,previous,next)
            print("prompt开始" + "_" * 40)
            print(prompt)
            print("prompt结束" + "_" * 40)
            # 1/0
            #prompt = f"""这是一本书中的一段文本，请纠正这段文本中的语法错误。返回处理后的结果。文本是:{content}，结果是："""
            #prompt=f"""这是一本书中的一段文字，请去除下列文本中多余的、不必要的换行符，但标题前的换行符要保留。返回repr的结果。文本是:{content}。"""
            #a=datetime.now()
            res=chat_with_6b(prompt)
            # previous = content
            #b=datetime.now()
            #sleep_time(a, b)#两次请求之间要相隔20s以上
            print(res)


#             print("去除多余换行符" + "_" * 100)
#             print(res)
#             # print(r'"{}"'.format(res))
#             1/0
#
#
#             #prompt = f"""修正下列文本中的错别字和语法错误。返回repr的结果。文本是:{res}。"""
#             #prompt = f"""这是一本书中的一部分文字，请找到它一级标题或二级标题或三级标题的位置，在位置处插入<titile>标记。返回repr的结果。文本是:{res}。"""
#             prompt = f"""这是一本书中的一部分文字，请找到这段文字中一级标题或二级标题，分别插入<section>、<subsection>标签，返回插入标签后的文本。文本是:{res}。"""
#
#
#             res = chat_with_chatpgt(prompt)
#             print("给标题加标签" + "_" * 100)
#             print(res)
#             #print(r'"{}"'.fa.ormat(res))
#
#             prompt = f"""这是一本书中的一部分文字，请修正下列文本中的错别字和语法错误，返回处理后的结果。但第一句话和最后一句话不用处理。文本是:{res}。"""
#             #prompt = f"""这是一本书中的一部分文字，请找到它一级标题或二级标题或三级标题的位置，在位置处插入<titile>标记。返回repr的结果。文本是:{res}。"""
#             #prompt = f"""这是一本书中的一部分文字，请找到它一级标题或二级标题或三级标题的位置，分别插入<section>、<subsection>、<subsubsection>标记，返回repr的结果。文本是:{res}。"""
#             res = chat_with_chatpgt(prompt)
#
#             print("语法纠错" + "_" * 100)
#             print(res)
#             #print(r'"{}"'.format(res))
#             1/0
#         if not content:
#             break
# content = file.read()
#
# file.close()
#
# print("①")
# # line = file.readline()
# # while line:
# #     print(line)
# #     line = file.readline()
