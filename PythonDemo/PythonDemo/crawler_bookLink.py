import requests
from bs4 import BeautifulSoup

#《妖神记》章节目录
bookNameUrl = "http://www.bxquge.com/6_6574/"
getUrl = requests.get(bookNameUrl)
getUrl.encoding = "utf-8"
bookListHtml = getUrl.text
#获得book页面Html
#print(bookListHtml)
soup = BeautifulSoup(bookListHtml,"html.parser")
bookList = soup.find(id="list")
#获取所有章节标签
#print(bookList)
chapterLink = bookList.find_all('a')
for link in chapterLink :
    print(link.string , bookNameUrl + link.get('href'))