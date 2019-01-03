
import random
import base64

from setting import USER_AGENTS, PROXIES

class RandomUserAgent(object):
    def process_request(self, equest, spider)

    useragent = random.choice(USER_AGENTS)
    request.headers.setdefault('User-Agent', useragent)

class RandomProxy(object):
    def process_request(self, request, spider)

    proxy = random.choice(PROXIES)

    if proxy['user_passwd'] is None:
        request.meta['proxy'] = 'http://' + proxy['ip_port']
    else:
        base64_userpasswd = base64.b64encode(proxy['user_passwd'])
        request.headers['Proxy-Authorization'] = 'Basic' + base64_userpasswd
        request.meta['proxy'] = 'http://' + proxy['ip_port']
