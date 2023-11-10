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
#df = pd.read_csv('./read_m4a.csv',encoding='ISO-8859-1')
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

url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + get_access_token()
def translate(txt):
    context= f'''根据提供的文本：先输出老人的姓名，然后根据提供的文本格式化地输出老人的健康情况，最后对这位老人的健康状况一个总结。文本是：{txt}'''
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

df["实体识别_文心一言"]=df["txt"].apply(translate)


df.to_csv('./实体识别_ChatGPT.csv', index=False,encoding='utf-8')