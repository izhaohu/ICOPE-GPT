#统计有多少字符
def count_characters_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return len(content)
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

file_path = "/opt/caregpt/text_tool/主动学习/chat_korean.txt"
char_count = count_characters_in_file(file_path)
if char_count is not None:
    print(f"The file {file_path} contains {char_count} characters.")
#contains 1508724 characters.
#ChatGPT API价格为1k tokens/$0.002
#约36元
#用百度翻译要375元
