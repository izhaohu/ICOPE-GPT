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
import requests
import json
# 文心一言
model='文心一言'
# model='bloomz'
#model='llama_2_7b'
#model='llama_2_13b'
model='chinese_llama_2_7b'

df = pd.read_csv('./实体识别_ChatGPT.csv',encoding='utf-8')

#鉴权
def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """

    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=xYijtMeM190xNw2G9eg2jE1R&client_secret=4rY59eZGezpsQW2iAZMBLyeQGvYpV8uH"

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")

if model=='文心一言':
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + get_access_token()
if model=='bloomz':
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/bloomz_7b1?access_token=" + get_access_token()
if model=='llama_2_7b':
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/llama_2_7b?access_token=" + get_access_token()
if model=='llama_2_13b':
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/llama_2_13b?access_token=" + get_access_token()
if model=='chinese_llama_2_7b':
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/qianfan_chinese_llama_2_7b?access_token=" + get_access_token()
def translate(txt):
    context= f'''给定一段文本：{txt}。
    根据提供的文本：第1步，输出老人的姓名；
    第2步，根据提供的文本格式化地输出老人的健康体征，健康体征可包括[体温，血氧饱和度，脉搏，血压，血糖，饮食，大便，小便，睡眠情况，身高，体重，小腿围，大腿围，外出情况，返院情况，皮肤，精神状况，其他情况],没有提及的字段不必输出。
    第3步，根据第2步的健康体征，罗列出异常的情况。
    第4步：根据第3步得到的异常情况给出照护或处理意见。
    '''
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": context
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    json_data =json.loads(response.text)
    # 获取 "result" 字段的值
    result_value = json_data["result"]
    # print(result_value)
    # 1/0
    return result_value

df["实体识别_"+model]=df["txt"].apply(translate)


df.to_csv('./实体识别_ChatGPT.csv', index=False,encoding='utf-8')