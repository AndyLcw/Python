
from urllib import request
import chardet

if __name__ == '__main__':
    response = request.urlopen("http://fanyi.baidu.com")
    html = response.read()
    # html =html.decode("utf-8")
    # print(html)
    ## 查看编码格式
    charsed = chardet.detect(html)
    print(charsed)