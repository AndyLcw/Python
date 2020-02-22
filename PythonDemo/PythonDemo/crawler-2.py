import requests

#我觉得这种写法很好
url = "http://www.bxquge.com/6_6574/79301.html"
response =  requests.get(url)
content = requests.get(url).content
#decode 与 charset=utf-8 有关
print(content.decode("utf-8"))
