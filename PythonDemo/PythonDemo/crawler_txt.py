from bs4 import BeautifulSoup
from urllib import request
import requests
import chardet

if  __name__ == "__main__":
 
    target = 'http://www.bxquge.com/6_6574/79301.html'
    req = requests.get(url=target)
    req.encoding = 'utf-8'
   # print(req.text)
    html = req.text
   # print(html)
    soup = BeautifulSoup(html,"html.parser")
   # print(soup)
    txt = soup.find_all('div',class_ = 'box_con')
    #txt = soup.find_all(soup.select('#content'))
    print(txt)