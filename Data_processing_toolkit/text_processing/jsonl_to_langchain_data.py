import json
import numpy as np
import os
input="./merged_output_ad.jsonl"
output="./langchain_input/merged_output_ad.txt"
if not os.path.exists("./langchain_input/"):
    os.makedirs("./langchain_input/")
with open(input, 'r') as f_in, open(output, 'w') as f_out:
    for i,line in enumerate(f_in):
        data = json.loads(line)
        question = data.get('question', '').replace('\n', '')
        answer = data.get('answer', '').lstrip('\n').replace('\n\n', '\n')
        if i in [17006,17007,17008]:
            print(r'{}'.format(question))
            print("====")
            print(r'{}'.format(answer))
            print("====")
        if str(question).endswith('\n'):
            f_out.write(question)
        else:
            f_out.write(question + '\n')
        if str(answer).endswith('\n'):
            f_out.write(answer + '\n')  # Add an extra newline to separate Q&A pairs
        else:
            f_out.write(answer + '\n\n')  # Add an extra newline to separate Q&A pairs
