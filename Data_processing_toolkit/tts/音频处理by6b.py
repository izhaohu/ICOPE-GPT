import pandas as pd
import requests
import json
url = "http://192.168.11.33:7861/chat"
headers = {"Content-Type": "application/json"}
# 读取CSV文件
#df = pd.read_csv('./read_m4a.csv',encoding='ISO-8859-1')
df = pd.read_csv('./read_m4a.csv',encoding='utf-8')

def translate(txt):
    data = {
        "question": f'''下列文本是语音识别的结果，内容是照护员录入长者的近况。请做文法更正：{txt}''',
        "history": []
    }
    gpt_response = requests.post(url=url, headers=headers, data=json.dumps(data))
    res=gpt_response.json()["response"]
    return res

df["语法纠正_6b"]=df["txt"].apply(translate)


df.to_csv('./语法纠正_6b.csv', index=False,encoding='utf-8')