
from urllib import request,parse,error
import json

'''
get request
'''
"""
if __name__ == '__main__':

    url = 'https://www.baidu.com/s?'
    wd = input('Input the Keyword: ')

    qs = {
        'wd': wd        
    }
    qs = parse.urlencode(qs)

    fullurl = url + qs
    response = request.urlopen(fullurl)
    html = response.read()
    #print(type(html))

    html = html.decode('utf-8')
    #print(html)

    print('URL: {}'.format(response.geturl()))
    print('Info: {}'.format(response.info()))
    print('Code: {}'.format(response.getcode()))
"""

'''
post request
'''
if __name__ == '__main__':
    
    base_url = 'http://fanyi.baidu.com/sug'

    kw = input('input the keyword: ')
    data = {
        'kw': kw        
    }
    data = parse.urlencode(data).encode('utf-8')

    #headers = {
    #    'Content-Length': len(data),
    #    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0'
    #}

    try:
        #req = request.Request(url=base_url, data=data, headers=headers)
        req = request.Request(base_url, data)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0')

        rsp = request.urlopen(req)

        result_json = rsp.read().decode('utf-8')

        result = json.loads(result_json)
        print(result) 
    except error.HTTPError as e:
        print('HTTPErroe: ', e)
    except error.URLError as e:
        print('URLError: {}'.format(e))
    except Exception as e:
        print(e)

'''
proxy
'''

"""
if __name__ == '__main__':

    url = 'http://www.baidu.com'

    proxy = {
        'http': '120.194.18.90:81'        
    }

    proxy_handler = request.ProxyHandler(proxy) 

    opener = request.build_opener(proxy_handler)

    request.install_opener(opener)

    try:
        rsp = request.urlopen(url)

        res = rsp.read().decode()

        print(res)
    except URLError as e:
        print('URLError: {}'.format(e))
    except HTTPError as e:
        print('HTTPError: {}'.format(e))
    except Exception as e:
        print(e)
"""







