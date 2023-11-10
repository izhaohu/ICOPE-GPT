import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service  = Service(executable_path='D:\chromedriver_win32\chromedriver.exe')

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service , options=options)

driver.get('https://www.mashangfangxin.com/')

# 找到输入框并输入追溯码
#input_element = driver.find_element_by_class_name('t-code')  # 替换为真实的输入框 HTML id
input_element = driver.find_element('class name','t-code')  # 替换为真实的输入框 HTML id
input_element.send_keys('83515410004748401667')  # 替换为你的追溯码
# 等待页面加载
driver.implicitly_wait(1000)

# 找到查询按钮并点击
button = driver.find_element('class name','code-btn')
button.click()

# 等待页面加载
driver.implicitly_wait(1000)

time.sleep(66)

# 获取返回的页面内容
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 在这里，你需要知道你想提取的数据在 HTML 中的标签和类名或 id
#data = soup.find('tag_name', attrs={'class': 'class_name'})  # 替换为真实的标签名和类名

print(html)

#driver.quit()
