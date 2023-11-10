import os
import platform
import signal
from transformers import AutoTokenizer, AutoModel
from peft import PeftModel
from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F
import readline
# os.environ["HTTP_PROXY"] = "http://192.168.11.33:7890"
# os.environ["HTTPS_PROXY"] = "http://192.168.11.33:7890"
tokenizer = AutoTokenizer.from_pretrained("/opt/weight/chatglm2-6b/", trust_remote_code=True)
model = AutoModel.from_pretrained("/opt/weight/chatglm2-6b/", trust_remote_code=True, device='cuda')
# 打印所有可训练的参数
for name, param in model.named_parameters():
    if param.requires_grad:
        print(f"{name}: {param.shape}")
1/0
#model = PeftModel.from_pretrained(model, "/opt/caregpt/LLM-Tuning/weights/caregpt_lora_weight/checkpoint-195000/").half()

# print(model.base_model.model.transformer.encoder.layers[27].self_attention.query_key_value.lora_B.default.weight)
# 1/0
# 多显卡支持，使用下面两行代替上面一行，将num_gpus改为你实际的显卡数量
# from utils import load_model_on_gpus
# model = load_model_on_gpus("THUDM/chatglm2-6b", num_gpus=2)
model = model.eval()

os_name = platform.system()
clear_command = 'cls' if os_name == 'Windows' else 'clear'
stop_stream = False


def build_prompt(history):
    prompt = "欢迎使用 ChatGLM2-6B 模型，输入内容即可进行对话，clear 清空对话历史，stop 终止程序"
    for query, response in history:
        prompt += f"\n\n用户：{query}"
        prompt += f"\n\nChatGLM2-6B：{response}"
    return prompt


def signal_handler(signal, frame):
    global stop_stream
    stop_stream = True


def main():
    past_key_values, history = None, []
    global stop_stream
    print("欢迎使用 ChatGLM2-6B 模型，输入内容即可进行对话，clear 清空对话历史，stop 终止程序")
    while True:
        #query = input("\n用户：")
        query = "照护员"
        if query.strip() == "stop":
            break
        if query.strip() == "clear":
            past_key_values, history = None, []
            os.system(clear_command)
            print("欢迎使用 ChatGLM2-6B 模型，输入内容即可进行对话，clear 清空对话历史，stop 终止程序")
            continue
        print("\nChatGLM：", end="")
        current_length = 0
        query = input("\n用户：")
########################3
        # 准备输入
        device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
        global model
        model = model.to(device)

        inputs = tokenizer("\n用户：感冒了怎么办？ \n回答：", return_tensors="pt")
        inputs = {key: value.to(device) for key, value in inputs.items()}
        # print(tokenizer.decode([64790, 64792, 24954]))
        # 1/0
        # 获取输出
        generation_output = model.generate(**inputs, return_dict_in_generate=True, output_scores=True, max_new_tokens=80)
        # 获取生成过程中的分数
        scores = generation_output.scores
        # 计算每一步的概率
        probabilities = [F.softmax(score, dim=-1) for score in scores]
        # 将令牌ID解码为字符串
        decoded_string = tokenizer.decode(generation_output.sequences[0], skip_special_tokens=True)
        print(len(generation_output.sequences[0]))
        print(len(probabilities))
        1/0
        # 打印生成的字符串
        print(decoded_string)
        print(probabilities)
        1/0

        outputs = model(**inputs)
        logits = outputs.logits
        # 计算每个令牌的概率分布
        probabilities = torch.nn.functional.softmax(logits, dim=-1)
        # 找到每个位置的最有可能的令牌ID
        predicted_ids = torch.argmax(probabilities, dim=-1)
        # 将令牌ID解码为字符串
        decoded_string = tokenizer.decode(predicted_ids[0], skip_special_tokens=True)

        print(decoded_string)


        # print(outputs)
        1/0
        # 这里是logits
        logits = outputs.logits

        #print(logits)
        print(logits.shape)


        #选择最可能的token ID

        probabilities = F.softmax(logits, dim=-1)
        predicted_ids = torch.argmax(probabilities, dim=-1)

        # 解码这些ID以获得文本
        decoded_string = tokenizer.decode(predicted_ids[0], skip_special_tokens=True)

        print(decoded_string)
        1/0

#########################3
        response, history = model.chat(tokenizer, query, history=[])
        #response=model(tokenizer, query)
        print(response)
        #print(response.logits)
        # for response, history, past_key_values in model.stream_chat(tokenizer, query, history=history,
        #                                                             past_key_values=past_key_values,
        #                                                             return_past_key_values=True):
        #     if stop_stream:
        #         stop_stream = False
        #         break
        #     else:
        #         print(response[current_length:], end="", flush=True)
        #         current_length = len(response)
        # print("")
        #return 0


if __name__ == "__main__":
    main()
