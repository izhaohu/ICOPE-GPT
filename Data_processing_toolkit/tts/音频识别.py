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
lfasr_host = 'https://raasr.xfyun.cn/v2/api'
# 请求的接口名
api_upload = '/upload'
api_get_result = '/getResult'
# openai.api_key = "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"
openai.api_key = "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"
os.environ["HTTP_PROXY"] = "http://192.168.11.33:7890"
os.environ["HTTPS_PROXY"] = "http://192.168.11.33:7890"
url = "http://192.168.11.33:7861/chat"
headers = {"Content-Type": "application/json"}
class RequestApi(object):
    def __init__(self, appid, secret_key, upload_file_path):
        self.appid = appid
        self.secret_key = secret_key
        self.upload_file_path = upload_file_path
        self.ts = str(int(time.time()))
        self.signa = self.get_signa()

    def get_signa(self):
        appid = self.appid
        secret_key = self.secret_key
        m2 = hashlib.md5()
        m2.update((appid + self.ts).encode('utf-8'))
        md5 = m2.hexdigest()
        md5 = bytes(md5, encoding='utf-8')
        # 以secret_key为key, 上面的md5为msg， 使用hashlib.sha1加密结果为signa
        signa = hmac.new(secret_key.encode('utf-8'), md5, hashlib.sha1).digest()
        signa = base64.b64encode(signa)
        signa = str(signa, 'utf-8')
        return signa


    def upload(self):
        print("上传部分：")
        upload_file_path = self.upload_file_path
        file_len = os.path.getsize(upload_file_path)
        file_name = os.path.basename(upload_file_path)

        param_dict = {}
        param_dict['appId'] = self.appid
        param_dict['languageType'] = 4
        param_dict['eng_vad_mdn'] = 2
        param_dict['eng_colloqproc'] = 1
        param_dict['signa'] = self.signa
        param_dict['ts'] = self.ts
        param_dict["fileSize"] = file_len
        param_dict["fileName"] = file_name
        param_dict["duration"] = "200"
        print("upload参数：", param_dict)
        data = open(upload_file_path, 'rb').read(file_len)

        response = requests.post(url =lfasr_host + api_upload+"?"+urllib.parse.urlencode(param_dict),
                                headers = {"Content-type":"application/json"},data=data)
        print("upload_url:",response.request.url)
        result = json.loads(response.text)
        print("upload resp:", result)
        return result


    def get_result(self):
        uploadresp = self.upload()
        orderId = uploadresp['content']['orderId']
        param_dict = {}
        param_dict['appId'] = self.appid
        param_dict['signa'] = self.signa
        param_dict['ts'] = self.ts
        param_dict['orderId'] = orderId
        param_dict['resultType'] = "transfer,predict"
        print("")
        print("查询部分：")
        print("get result参数：", param_dict)
        status = 3
        # 建议使用回调的方式查询结果，查询接口有请求频率限制
        while status == 3:
            response = requests.post(url=lfasr_host + api_get_result + "?" + urllib.parse.urlencode(param_dict),
                                     headers={"Content-type": "application/json"})
            # print("get_result_url:",response.request.url)
            result = json.loads(response.text)
            print(result)
            status = result['content']['orderInfo']['status']
            print("status=",status)
            if status == 4:
                break
            time.sleep(5)
        print("get_result resp:",result)
        return result


def extract_sentence_from_xunfei(data):
    # 先解析外层的orderResult
    order_result_str = data.get("orderResult", "{}")
    order_result = json.loads(order_result_str)

    # 提取所有的词汇
    words = []
    for lattice in order_result.get("lattice", []):
        json_1best = json.loads(lattice.get("json_1best", "{}"))
        for rt in json_1best.get("st", {}).get("rt", []):
            for ws in rt.get("ws", []):
                for cw in ws.get("cw", []):
                    word = cw.get("w", "")
                    words.append(word)

    # 组合词汇为句子
    sentence = "".join(words)

    return sentence
def save_to_txt(content, filename="output.txt"):
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(content)

# 输入讯飞开放平台的appid，secret_key和待转写的文件路径
if __name__ == '__main__':
    # 设定目录路径
    dir_path = './音频/'
    # 创建DataFrame
    df = pd.DataFrame(columns=['name', 'txt'])
    for filename in os.listdir(dir_path):
        api = RequestApi(appid="edb475d9",
                         secret_key="4a844726c919f9f8e57f2915c8a85d76",
                         upload_file_path=fr"./音频/{filename}")
        data=api.get_result()
        sentence = extract_sentence_from_xunfei(data['content'])
        # 添加新的数据到DataFrame末尾
        df.loc[len(df)] = [filename, sentence]
        # print(df)
        # 1/0

    # 保存到CSV文件
    df.to_csv('read_m4a.csv', index=False, encoding='utf-8-sig')

    #standard = '''北风和太阳在那儿争论谁的本事大，争来争去分不出个高低来，这时候路上来了个走道儿的，他身上穿了一件厚大衣，两个人说好谁能叫这个走道儿的先脱掉那件大衣，就算谁的本事大。北风就拼命刮起来了。但是他越是刮得厉害，那个走道儿的把大衣裹得越紧，过了一会儿太阳出来了，他火辣辣的一晒，那个走道儿的马上就把那件厚大衣脱下来了。那么北风和太阳比还是太阳的本事大。'''

    # 输出: 中心经委7月15
#################################################################################################################
    #context = f'''把第二段文本中所有和第一段不一致的地方列出来。第一段文本是：{standard}，第二段文本是：{sentence}'''
    # context = f'''为了测试患者的认知能力，让患者照着原文念了一遍。原文是：{standard}，患者念的结果是：{sentence}。请列出患者哪些地方念得和原文不一样？再比较内容1和内容二的相似度，给出相似度的分值，分支从 0 - 100，100是百分百相似。最后请评价一下患者的认知能力。'''
    # messages=[]
    # messages.append({"role": "user", "content": context})
    # completions = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     #max_tokens=115,
    #     temperature=0.1,
    #     top_p=0.1,
    #     messages=messages)
    # gpt_response = completions.choices[0]['message']
    # res = '长者的语音：\n\n' + sentence + '\n\n' + '对比结果：\n\n' + gpt_response["content"]
    # #################################################################################################################
    #
    # # data = {
    # #     "question": f'''第一段文本是标准文本，第二段是认知症老人念的，请问老人哪些地方念错了？第一段文本是：{standard}，第二段文本是：{sentence}''',
    # #     "history": []
    # # }
    # # gpt_response = requests.post(url=url, headers=headers, data=json.dumps(data))
    # # res='长者的语音：\n\n'+sentence+'\n\n'+'对比结果：\n\n'+gpt_response.json()["response"]
    # #################################################################################################################
    #
    #
    # #save_to_txt(gpt_response.json()["response"], "result.txt")
    # save_to_txt(res, "result.txt")
    #
    #
    #
    #
