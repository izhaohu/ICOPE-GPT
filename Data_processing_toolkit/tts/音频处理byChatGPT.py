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
df = pd.read_csv('./语法纠正_6b.csv',encoding='utf-8')

def translate(txt):
    context= f'''对语言识别的结果做语法修正，删除多余的部分，添加遗漏的部分，直接返回结果。文本是：{txt}'''
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

df["语法纠正_chatgpt"]=df["txt"].apply(translate)


df.to_csv('./语法纠正_ChatGPT.csv', index=False,encoding='utf-8')