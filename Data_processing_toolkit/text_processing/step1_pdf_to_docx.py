import base64
import urllib
import requests

import base64
import urllib
import requests

API_KEY = "2PvPjsd6BQPyS1NO0wPUAeal"
SECRET_KEY = "5811DTeY5Rd4amLGui3yiIxTIT7yCyZl"
pdf_dir="/opt/caregpt/text_tool/老年长期照护与康复指导手册 - 缪荣明.pdf"#_1-241


def main():

    base64=get_file_content_as_base64(pdf_dir,1)#获取文件64编码
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/doc_convert/request?access_token=" + get_access_token()
    payload = f'''pdf_file={base64}'''
    # pdf_file 可以通过 get_file_content_as_base64("C:\fakepath\老年长期照护与康复指导手册 - 缪荣明_1-241.pdf",True) 方法获取
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    main()
