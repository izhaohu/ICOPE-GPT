def remove_empty_lines(file_path):
    # 读取Markdown文件内容
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 移除空行和无关内容
    filtered_lines = []
    for line in lines:
        #line = line.strip()  # 去除行首和行尾的空白字符
        if line:  # 非空行且不以 '#' 开头
            filtered_lines.append(line)

    # 保存处理后的Markdown文件
    output_file_path = file_path[:-3] + '_去空行.md'
    with open(output_file_path, 'w') as file:
        file.write('\n'.join(filtered_lines))

    return output_file_path


# 使用示例
markdown_file_path = '/opt/caregpt/text_tool/output/老年长期照护与康复指导手册_去目录.md'
processed_file_path = remove_empty_lines(markdown_file_path)
print(f"处理后的文件保存在: {processed_file_path}")
