import os
import time

import requests
import json

url = "http://192.168.11.201:7861/chat/chat"
# url2 = "http://192.168.11.33:7861/local_doc_qa/local_doc_chat"
# url3 = "http://192.168.11.33:7861/local_doc_qa/bing_search_chat"
headers = {"Content-Type": "application/json"}

#设置代理远程服务器
# os.environ["HTTP_PROXY"] = "http://192.168.11.33:7890"
# os.environ["HTTPS_PROXY"] = "http://192.168.11.33:7890"

q='''你是一位照护长，请对老人出现的健康情况做分析，并向照护员提出合理的照护建议。老人的情况是：{"义齿":"无","人群标签":"失智","人际关系":"可","修饰":"完全依赖","喜好":"唱歌、跳舞","如厕":"需帮助","姓名":"徐克环","婚姻状况":"离婚","子女数量":"1","学历":"本科","宗教信仰":"无","家属关心程度":"不详","家属史":"女儿患阿尔兹海默氏病","家属期望":"降低家庭照护负担","心里创伤":"有2002年儿子去世、女儿患AD","性别":"女","教育年限":"0","既往史":"阿尔茨海默病（幻觉错觉），高血压，抑郁（儿子02年去世，女儿患AD），甲减，尿路感染，骨质疏松","是否有精神行为表现":"否","是否离退休干部":"否","是否离退休老人":"是","民族":"汉族","沟通能力":"偶尔沟通困难","洗澡":"完全依赖","照护难度系数":"一般","现病":"阿尔茨海默病、高血压、骨质疏松","生日":"1936-10-09","用餐":"其他","穿衣":"需帮助","管路":"不需要","精神行为标签":"异常运动行为、幻觉","约束状态":"无","纸尿裤":"晚上穿","药物服务配合度":"可配合","药物服用方式":"合在饭内","萤火虫事件事件发生状态":"集体服务","萤火虫事件事件描述":"长者徐克环在卫生间如厕，其他认知症长者拉扶过程中坐倒在地，未造成伤害","萤火虫事件分类":"厕所内跌倒","萤火虫事件发生时间":"2023-10-08 06:02:00","萤火虫事件后果":"无异常","萤火虫事件就医情况":"未就医","萤火虫事件根因分析":"照护员要时刻关注到老人们的动向","萤火虫事件症状表现":"无症状","认知症类型":"阿尔茨海默病","进食方式":"自理","退休工资":"8000以上","配合程度":"安心","重点观察老人":"是"}'''
data = {
  "query": q,
  "history": [],
  "stream": False,
  "model_name": "baichuan-13b-chat",
  "temperature": 0.2,
  "max_tokens": 800,
  "prompt_name": "default"
}


def chat(url, headers, data):
  response = requests.post(url=url, headers=headers, data=json.dumps(data))

  if response.status_code == 200:
    # 如果 Content-Type 是 application/json，则尝试解析 JSON
    if 'application/json' in response.headers['Content-Type']:
      try:
        return response.json()
      except json.JSONDecodeError:
        print("Failed to decode JSON.")
    # 如果不是 JSON，则直接返回文本内容
    return response.text
  elif response.status_code == 422:
    # 对于验证错误，尝试解析和返回 JSON 错误详情
    try:
      return response.json()
    except json.JSONDecodeError:
      print("Failed to decode JSON.")
      return response.text
  else:
    # 对于其他状态码，返回错误信息
    return f"Error: {response.status_code}, {response.text}"

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
r=chat(url,headers,data)
print(r)
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