#把空行替换为***********************为了解决langchain的问题
root='/opt/caregpt/text_tool/langchain_input/'
input_file=root+'merged_output_dyrmyy.txt'
output_file=root+input_file.split("/")[-1].split(".")[0]+'-no_blank.txt'
print(output_file)



with open(input_file, 'r',encoding='utf-8') as file:
    lines = file.readlines()

with open(output_file, 'w',encoding='utf-8') as file:
    for line in lines:
        if line.strip() == '':
            file.write('*'*300+'\n')
        else:
            file.write(line)
