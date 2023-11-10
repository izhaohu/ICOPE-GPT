import os
from datetime import datetime
import traceback
import fitz  # PyMuPDF
import io
import time
from PIL import Image
import concurrent.futures
import openai
import re
import os
import openai
import sys
import threading
import gc
import concurrent.futures
#设置代理远程服务器
os.environ["HTTP_PROXY"] = "http://192.168.11.33:7890"
os.environ["HTTPS_PROXY"] = "http://192.168.11.33:7890"
#API key  企业
openai.api_key = "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"


def chat_with_chatpgt(context:str,messages_history=None):
    # 调用 OpenAI ChatGPT 模型
    if not messages_history:
        messages=[
        {"role": "system", "content": "翻译员"},
        {"role": "user", "content": context}]
    else:
        # print(messages_history)
        # 1/0
        messages_history.append({"role": "user", "content": context})
        messages=messages_history.copy()
    #print(messages)
    completions = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      max_tokens=45,
      temperature =0,
      top_p=0,
      messages=messages)
    gpt_response=completions.choices[0]['message']
    messages.append({"role": "system", "content": gpt_response["content"]})
    return gpt_response["content"]

count=1
def main():
    input_path = "/opt/caregpt/text_tool/主动学习/chat_korean.txt"
    output_path = "/opt/caregpt/text_tool/主动学习/chat_chinese.txt"
    last_successful_line = 0
    while True:
        try:
            with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'a', encoding='utf-8') as outfile:
                lines = infile.readlines()
                for idx, line in enumerate(lines):

                    if idx < last_successful_line:  # Skip lines up to the last successful one
                        continue
                    #print(idx)
                    line = line.strip()
                    if not line:
                        global count
                        count+=1
                        print("对话轮次："+str(count))
                        outfile.write("\n")
                    else:
                        prompt = f'将文本翻译为中文，直接返回译文，禁止添加多余的内容,返回结果不要换行，答案不要出现韩语；文本为：{line}'
                        translation = chat_with_chatpgt(context=prompt)
                        # if (last_successful_line) % 8==0:
                        #     1 / 0
                        print(translation)
                        outfile.write(translation + "\n")
                        #time.sleep(1)
                    last_successful_line = idx  # Update the last successful line
            break  # Exit the while loop if everything is successful

        except Exception as e:
            print(f"Error encountered: {e}")
            traceback.print_exc()
            print("Waiting...")
            time.sleep(60)
            last_successful_line+=1
            continue


if __name__ == "__main__":
    main()

