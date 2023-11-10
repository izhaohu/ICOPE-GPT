from mistune import markdown
file_out="/opt/caregpt/text_tool/老年长期照护与康复指导手册-step1语法纠正.txt"
markdown_content = markdown(file_out)

with open(file_out, 'r') as file:
    text = file.read()
file.close()


with open('output.md', 'w') as file:
    file.write(text)
file.close()