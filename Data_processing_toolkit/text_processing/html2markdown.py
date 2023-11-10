#这段代码实现了docx转换为html再转换为MarkDown的过程
#使得结构化文本保留了图片、表格等样式。
import pypandoc

html_file_path="/opt/caregpt/text_tool/老年长期照护与康复指导手册html.html"
markdown_file_path="/opt/caregpt/text_tool/output/老年长期照护与康复指导手册html.md"

# 将 HTML 转换为 Markdown
output = pypandoc.convert_file(html_file_path, "md")

# 将 Markdown 内容写入文件
with open(markdown_file_path, "w") as markdown_file:
    markdown_file.write(output)

print("转换完成！")


