import requests , sys
from bs4 import BeautifulSoup

"""
类说明：下载“新笔趣阁”网小说《妖神记》
"""

class downloader(object):

    def __init__(self):
        self.bookNameUrl = "http://www.bxquge.com/6_6574/"
        self.chapterName = []      #章节名
        self.chapterUrl = []     #章节链接
        self.nums = 0           #章节数

    """
    函数说明：获取下载链接
    """
    def get_download_url(self):
        getUrl = requests.get(url = self.bookNameUrl)
        getUrl.encoding = "utf-8"
        bookListHtml = getUrl.text
        soup = BeautifulSoup(bookListHtml,"html.parser")
        bookList = soup.find(id="list")
        chapterLink = bookList.find_all('a')
        self.nums = len(chapterLink)
        for link in chapterLink:
            self.chapterName.append(link.string)
            self.chapterUrl.append(self.bookNameUrl + link.get('href'))

    """
    函数说明：获取章节内容
    """
    def get_contents(self,chapterLink):
        getUrl = requests.get(url = chapterLink)
        getUrl.encoding = "utf-8"
        bookListHtml = getUrl.text
        soup = BeautifulSoup(bookListHtml,"html.parser")
        text = soup.find_all(id='content')
        texts = text[0].text.replace('readx();','\n')
        texts = texts.replace('\xa0'*4,'\n\n')
        return texts

    """
    函数说明：将爬取的文章内容写入文件
    paramaters：
        name - 章节名称
        path - 当前路径下，小说保存名称
        text - 章节内容
    """
    def writer(self,name,path,text):
        write_flag = True
        with open(path,'a',encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == "__main__":
    dl =  downloader()
    dl.get_download_url()
    print("《妖神记》开始下载：")
    for i in range(dl.nums):
        dl.writer(dl.chapterName[i],"妖神记.txt",dl.get_contents(dl.chapterUrl[i]))
        sys.stdout.write("已下载：%.3f%%" % float(i/dl.nums*100) + '\r')
        sys.stdout.flush()
    print("《妖神记》下载完成！")