# -*- coding: utf-8 -*-
import base64
import hashlib
import hmac
import json
import os
import time

import pandas as pd
import requests
import urllib
import os
import openai
openai.api_key = "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"
os.environ["HTTP_PROXY"] = "http://192.168.11.33:7890"
os.environ["HTTPS_PROXY"] = "http://192.168.11.33:7890"
# 读取CSV文件
#df = pd.read_csv('./read_m4a.csv',encoding='ISO-8859-1')
df = pd.read_csv('./语法纠正_ChatGPT.csv',encoding='utf-8')

def translate(txt):
    context= f'''给定一段文本：{txt}。
    根据提供的文本：第1步，输出老人的姓名；
    第2步，根据提供的文本格式化地输出老人的健康体征，健康体征可包括[体温，血氧饱和度，脉搏，血压，血糖，饮食，大便，小便，睡眠情况，身高，体重，小腿围，大腿围，外出情况，返院情况，皮肤，精神状况，其他异常],没有提及的字段不必输出。
    第3步，根据第2步的健康体征，罗列出异常的情况。
    第4步：根据第3步得到的异常情况给出照护或处理意见。
    '''
    messages = []
    messages.append({"role": "user", "content": context})
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # max_tokens=115,
        temperature=0.1,
        top_p=0.1,
        messages=messages)
    gpt_response = completions.choices[0]['message']
    print(gpt_response["content"])
    return gpt_response["content"]

df["实体识别_chatgpt"]=df["txt"].apply(translate)


df.to_csv('./实体识别_ChatGPT.csv', index=False,encoding='utf-8')