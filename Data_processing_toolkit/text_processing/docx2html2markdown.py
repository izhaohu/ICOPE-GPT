#这段代码实现了docx转换为html再转换为MarkDown的过程
#使得结构化文本保留了图片、表格等样式。
from mistune import markdown
import mammoth
from markdownify import markdownify
import os
from pathlib import Path
import time
import requests
from markdownify import markdownify
import re
#input="/opt/caregpt/text_tool/input/老年长期照护与康复指导手册 - 缪荣明_ppstructure.docx"
input="/opt/caregpt/text_tool/input/老年长期照护与康复指导手册 - 缪荣明.docx"
#input="/opt/caregpt/text_tool/input/老年长期照护与康复指导手册wps.docx"
output_name=input.split("/")[-1].split(".")[0]
# print(output_name)
# 1/0
def MD(input):
    with open(input, "rb") as docx_file:
        # 转化Word文档为HTML
        result = mammoth.convert_to_html(docx_file, convert_image=mammoth.images.img_element(convert_img))
        #time.sleep(2)
        #result = mammoth.convert_to_html(docx_file)
        # 获取HTML内容
        html = result.value
        html=process_image_tags(html)
        # print(html)#发病后6小时以内进行溶栓使血管再
        # 1/0
        # 转化HTML为Markdown
        md = markdownify(html,heading_style="ATX")
        with open(f'''/opt/caregpt/text_tool/output/{output_name}.md''', "w",encoding='utf-8') as md_file:
            # html_file.write(html)
            md_file.write(md)

            print("MD转换成功")
            #print(md[:1000])
        #messages = result.messages

# 转存Word文档内的图片
def convert_img(image):
    with image.open() as image_bytes:
        file_suffix = image.content_type.split("/")[1]
        # word中图片转为的目录,如果不存在则新建
        my_img = Path("./output/img")
        if my_img.is_dir()==0:
            os.makedirs("./output/img")
        path_file = "./output/img/{}.{}".format(str(time.time()).split(".")[-1],file_suffix)

        # print(path_file)
        # 1/0
        with open(path_file, 'wb') as f:
            f.write(image_bytes.read())
    return {"src":path_file}

def process_image_tags(html):
    # 从HTML中提取所有<img>标签的src属性值
    image_tags = re.findall(r'<img.*?src=["\'](.*?)["\'].*?>', html)
    # print(image_tags)
    # 1/0

    for img_src in image_tags:
        # 下载图片
        #print(img_src)


        ###以下：下载网络照片到本地
        #response = requests.get(img_src)
        #response = requests.get("/opt/caregpt/text_tool/img/723157.jpeg")
        # if response.status_code == 200:
        #     # 保存图片到本地
        #     filename = img_src.split('/')[-1]
        #     with open(filename, 'wb') as file:
        #         file.write(response.content)
        #     # 替换HTML中的<img>标签为Markdown格式
        # markdown_image = f"![Image]({img_src})"
        # html = html.replace(f'<img src="{img_src}"/>', markdown_image)
        markdown_image = f'''![Image]({img_src})'''
        # print(img_src)
        # print(markdown_image)
        # print(f'''<img src="{img_src}"/>''')
        # 1/0
        #print(html[:500])
        html = html.replace(f'''<img src="{img_src}"/>''', markdown_image)
        html = html.replace(f'''<img src="{img_src}" />''', markdown_image)
        #print(html[:500])

    return html

if __name__ == '__main__':
    MD(input)

