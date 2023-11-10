import os
import time

import requests
import json

url = "http://192.168.11.33:7861/chat"
url2 = "http://192.168.11.33:7861/local_doc_qa/local_doc_chat"
url3 = "http://192.168.11.33:7861/local_doc_qa/bing_search_chat"
headers = {"Content-Type": "application/json"}

#设置代理远程服务器
os.environ["HTTP_PROXY"] = "http://192.168.11.33:7890"
os.environ["HTTPS_PROXY"] = "http://192.168.11.33:7890"

data = {
  "knowledge_base_id":"tjl",
  "question": "对于拒绝食物的老人，如何确保老人的营养和饮食需求得到满足？",
  "history": []
}

def chat(url,headers,data):
  response = requests.post(url=url, headers=headers, data=json.dumps(data))
  return response
  # 输出服务器响应
  # print(response.json()["question"])
  # print(response.json()["response"])

def chat_knowledge(url2,headers,data):
  response = requests.post(url=url2, headers=headers, data=json.dumps(data))
  return response
  # 输出服务器响应
  # print(response.json())
  # print(response.json()["question"])
  # print(response.json()["response"])
def chat_bing(url3,headers,data):
  data['question'] = data['question'][:200]
  response = requests.post(url=url3, headers=headers, data=json.dumps(data))
  #print(response)
  return response

#加载Lora ,不加载Lora
#不用知识库
# chat(url,headers,data)
# #用知识库
# chat_knowledge(url2,headers,data)
#
# chat_bing(url3,headers,data)
# time.sleep(3)
# chat_bing(url3,headers,data)
# time.sleep(3)
#
# chat_bing(url3,headers,data)
# time.sleep(3)
# chat_bing(url3,headers,data)
# time.sleep(3)
# chat_bing(url3,headers,data)
# time.sleep(3)
# chat_bing(url3,headers,data)
# time.sleep(3)
# chat_bing(url3,headers,data)
# time.sleep(3)