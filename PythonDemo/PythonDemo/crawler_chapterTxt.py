from bs4 import BeautifulSoup
import requests

url = "http://www.bxquge.com/6_6574/79301.html"
response = requests.get(url)
response.encoding ="utf-8"
html = response.text
#print(html)
soup = BeautifulSoup(html,"html.parser")
head = soup.head
#print(head)
## #tag的 .contents 属性可以将tag的子节点以列表的方式输出
head_list = head.contents
#print(head_list)
"""
print(head_list[1])
print(head_list[1].name)
print(head_list[1].contents)
"""

'''
print(head_list[0])
print(head_list[0].name)
# 字符串没有 .contents 属性,因为字符串没有子节点
print(head_list[0].contents)

'''

body = soup.body
#print(body)
div = soup.div
#print(div)
## #通过点取属性的方式只能获得当前名字的第一个tag
script = soup.script
#print(script)

###测试
title = soup.h1
print(title.text)

text = soup.find_all(id='content')
## #find_all匹配的返回的结果是一个列表。提取匹配结果后，使用text属性，提取文本内容，滤除br标签。随后使用replace方法，剔除空格，替换为回车进行分段。
texts = text[0].text.replace('readx();','\n')
texts = texts.replace('\xa0'*4,'\n\n')
print(texts)
#print(text[0].text.replace('\xa0'*4,'\n\n'))

