
from urllib import request
from urllib import parse
import json

if __name__ == "__main__":
    #请求Request URL
    Request_URL = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    #创建From_Data字典，存储From Data
    Form_Data = {}
    Form_Data['from'] = 'AUTO'
    Form_Data['to'] = 'AUTO'
    Form_Data['i'] = 'jack'
    Form_Data['smartresult'] = 'dict'
    Form_Data['client'] = 'fanyideskweb'
    Form_Data['salt'] = '15816827540453'
    Form_Data['sign'] = '8744e99d45e70d4d594c69c36dbe0716'
    Form_Data['ts'] = '1581682754045'
    Form_Data['bv'] = '901200199a98c590144a961dac532964'
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['action'] = 'FY_BY_REALTlME'
    #使用urlencode方法转换标准格式
    data = parse.urlencode(Form_Data).encode('utf-8')
    #传递Request对象和转换完格式的数据
    response = request.urlopen(Request_URL,data)
    #读取信息并解码
    html = response.read().decode('utf-8')
    #使用JSON
    translate_results = json.loads(html)
    print(translate_results)
    print(translate_results['translateResult'])
    print(translate_results['translateResult'][0])
    print(translate_results['translateResult'][0][0])
    #找到翻译结果
    translate_results = translate_results['translateResult'][0][0]['tgt']
    #打印翻译信息
    print("翻译的结果是：%s" % translate_results)    

