
# break youdao

from urllib import request, parse

def getSalt():
    import time, random

    salt = int(time.time() * 1000) + random.randint(0, 10)

    return salt

def getMd5(v):
    import hashlib

    md5 = hashlib.md5()
    md5.update(v.encode('utf-8'))

    sign = md5.hexdigest()
    return sign

def getSign(key, salt):
    
    sign = 'fanyideskweb' + key + str(salt) + 'ebSeFb%=XZ%T[KZ)c(sy!'
    return sign

def youdao(kw):

    salt = getSalt()

    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    data = {
        'i': kw,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': str(salt),
        'sign': str(getSign(kw, salt)),
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typeResult': 'false'
    }
    data = parse.urlencode(data).encode()

    headers = {
        'Content-Length': len(data) 
    }

    rsq = request.Request(url, data,headers)

    rsp = request.urlopen(rsq)

    result = rsp.read().decode()
    return result

youdao('girl')

