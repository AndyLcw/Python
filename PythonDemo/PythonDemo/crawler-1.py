
from urllib import request
import chardet
import requests


if __name__ == '__main__':
    #乱码情况
    rawdata = request.urlopen('http://www.bxquge.com/6_6574/79301.html').read()
    rawdata = chardet.detect(rawdata)
    print(rawdata)
    #{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
    target = 'http://www.bxquge.com/6_6574/79301.html'
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    print(req.text)
