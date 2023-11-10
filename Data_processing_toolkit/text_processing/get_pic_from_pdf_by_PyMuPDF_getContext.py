import os
import fitz  # PyMuPDF
import io
import time
from PIL import Image
import re
import os
import openai
import json
# 主要功能:PDF文件中提取图片并为其分配适当的标题。
# 具体来说，代码首先使用 PyMuPDF 库（在这里被导入为 fitz）打开一个 PDF 文件。然后，它遍历文档的每一页，对于每一页，它获取所有的文本块和图片。
# 对于每个图片，它首先找出图片的坐标。然后，它检查每一个文本块，如果这个文本块的位置和图片的位置在垂直方向上接近，且文本块中包含'表'或者'图'且没有句号，那么就认为这个文本块是图片的标题。
# 如果在当前页没有找到图片的标题，那么会考虑上一页的最后一个文本块是否符合标题的条件。
# 初始化存储结果的字典
result_dict = {}
pdf_file = "./input/血管通电子书_ocr.pdf"
img_folder = './output/'+pdf_file.split("/")[-1].split(".")[0]+'/'
# print(img_folder)
# 1/0
doc = fitz.open(pdf_file)

def is_nearby(block_bbox, img_bbox, tolerance=35):
    #print(str(block_bbox)+"---"+str(img_bbox))
    # 判断文本块是否在图片的上方或下方并且他们的左右位置大致相同
    x0, y0, x1, y1 = block_bbox
    x0_, y0_, x1_, y1_ = img_bbox
    #[x0, y0, x1, y1] x0, y0：矩形左下角的坐标 x1, y1：矩形右上角的坐标
    # if abs(block_left - img_left) <= tolerance and abs(block_right - img_right) <= tolerance:
    #     if abs(block_bottom - img_top) <= tolerance or abs(block_top - img_bottom) <= tolerance:
    #         return True
    # print(abs(y1-y0_))
    # print(abs(y0-y1_))
    if abs(y1-y0_)<= tolerance:
        return True
    elif abs(y0-y1_)<= tolerance:
        return True
    return False
templast=''#上一页最后一段文本
for i in range(len(doc)):
    #print("index"+str(i))
    # 获取每页的文本块
    blocks = doc[i].get_text("blocks")

    # print(blocks)# (106.99220275878906, 208.45755004882812, 283.0654602050781, 224.88389587402344, '图书在版编目（CIP）数据\n', 1, 0)
    # 1/0
    page=doc.load_page(i)#获取页面
    image_list=page.get_images(full=True)  # 获取页面中图片信息
    # print(image_list)#[(2139, 0, 700, 1026, 8, 'DeviceRGB', '', 'Image0', 'DCTDecode', 0)]
    # 1/0
    # print(image_list)
    # 1/0
    for number,img in enumerate(image_list):
        #print(img)
        # 1/0
        xref = img[0]#图片xref
        #print(xref)
        pic_position = page.get_image_info(xref)[number]["bbox"]# # 图像的坐标
        #print(page.get_image_info(xref))
        # if i==1 or i==0:
        #print(pic_position)

        img_title = str(time.time()).split(".")[-1]
        random_data=str(time.time()).split(".")[-1]
        flag=0 #没有找到图片标题
        for block in blocks:
            original_block = block
            # 获取文本块的位置信息
            block_bbox = block[:4]
            # print(block[4])
            # print(">>>>>>>>")
            block_text = block[4]

            # 如果文本块在图片的上方或下方，并且他们的左右位置大致相同
            print(">>>>>>>>")
            print(repr(block[4]))
            print(">>>>>>>>")
            print(is_nearby(block_bbox, pic_position))
            print(">>>>>>>>")
            match1 = '(?s)^(?!.*[/，,。]).{0,29}(表|图).{0,29}$'
            # match1 = '(?s)^(?!.*[/])(?=.*-).{0,29}(表|图).{0,29}$'


            #初步过滤：以任意字符开头，包含表或图，表或图后面最多有20个字符，且不含/。，、
            # match2 = r'.*(?=表|图)[^/。，、]{0,20}'  # 以表或图开头，匹配最多30个字符，不包含/。，、
            # match3 = r'.*(?=表|图)[^/。，、]{0,20}'              #得到子串：以表或图开头
            # match_str=r'^[^/。，、]{0,50}(?:表|图)[^/。，、]{0,50}$'
            # match_str_temp = r'^(?:表|图)[^/。，、]{0,50}$'
            # str =

            print(re.search(match1, block[4]))
            # print("xxxxxx")
            print(">>>>>>>>")
            #从字符图和表切割到最后
            # 对文本块，从第一个出现图或表的字符开始切分，到文本块末端。
            result = ""
            s = block[4]
            index_of_tu = s.find('图')
            index_of_biao = s.find('表')
            # 获取第一个出现的位置
            if index_of_tu == -1:
                start_index = index_of_biao
            elif index_of_biao == -1:
                start_index = index_of_tu
            else:
                start_index = min(index_of_tu, index_of_biao)
            # 从该位置开始截取字符串到最后
            if start_index != -1:
                result = s[start_index:]
            modified_block = list(block)
            modified_block[4] = result
            block = tuple(modified_block)
            #print(block[4])
            #找到字符串block_text中第一个出现的"表"或"图"字符，并根据给出的正则表达式规则检查该字符串是否与这个正则匹配。如果匹配，你希望删除该位置之前的所有字符。
            #re.search(r'^.{0,29}(?:表|图).{0,29}$', block[4])
            if is_nearby(block_bbox, pic_position) and re.search(match1, block[4]):
                # 这个文本块可能就是这个图片的标题
                #print(block[4])
                img_title = block[4]
                flag=1#找到图片标题

                # 获取上下文
                block_index = blocks.index(original_block)
                # context_before = blocks[block_index - 1][4] if block_index > 0 else ""
                # context_after = blocks[block_index + 1][4] if block_index < len(blocks) - 1 else ""
                full_text = ' '.join([b[4] for b in blocks])
                title_position = full_text.find(img_title)
                start = max(0, title_position - 300)
                end = min(len(full_text), title_position + len(img_title) + 300)
                context_before = full_text[start:title_position]
                context_after = full_text[title_position + len(img_title):end]
                # 保存到字典
                result_dict[base] = {
                    "base": base,
                    "context_before": context_before[:250],  # 获取前50个字符
                    "context_after": context_after[:250]  # 获取后50个字符
                }

                break #已经找到了图片标题，跳出for循环
                #print(block[4])

        # 找上一页最后一段文本是不是图片标题
        # 对文本块，从第一个出现图或表的字符开始切分，到文本块末端。
        if flag == 0:
            result = ""
            s = templast
            index_of_tu = s.find('图')
            index_of_biao = s.find('表')
            # 获取第一个出现的位置
            if index_of_tu == -1:
                start_index = index_of_biao
            elif index_of_biao == -1:
                start_index = index_of_tu
            else:
                start_index = min(index_of_tu, index_of_biao)
            # 从该位置开始截取字符串到最后
            if start_index != -1:
                result = s[start_index:]
            templast = s
        if flag==0 and re.search(match1, templast):
            # print(re.search(r'^.{0,29}(?:表|图).{0,29}$', templast))

            img_title = templast
            flag = 1


        img_title=re.sub(r"\s+", "_", img_title)#去掉空字符串
        base =pdf_file.split(".")[0]+"_"+  img_title+"_"+random_data+ ".png"
        print(base)

        pix = fitz.Pixmap(doc, xref)
        if pix.n < 5:  # this is GRAY or RGB
            pass
        else:  # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix = pix1
        img_data = pix.tobytes()

        img = Image.open(io.BytesIO(img_data))

        # Create image directory if it doesn't exist
        if not os.path.exists(img_folder):
            os.makedirs(img_folder)

        # Save image to the directory
        img_path = os.path.join(img_folder, str(base))
        # print(img_folder)
        # 1/0
        img.save(img_path)
        #time.sleep(1)

    templast = blocks[-1][4]  # 上一页的最后一个文本

# Save the modified PDF



# 保存结果到 JSON 文件
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(result_dict, f, ensure_ascii=False, indent=4)