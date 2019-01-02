
from urllib import request, parse
from http import cookiejar

#create object
#cookie = cookiejar.CookieJar()

filename = 'cookie.txt'
cookie = cookiejar.MozillaCookieJar(filename)

#make cookie processor
cookie_handler = request.HTTPCookieProcessor(cookie)

#create http handler
http_handler = request.HTTPHandler()

#create https handler
https_handler = request.HTTPSHandler()

#bulid opener
opener = request.build_opener(http_handler, https_handler, cookie_handler)

'''
 get cookie
'''
def login():

    url = 'http://www.renren.com/PLogin.do'

    data = {
        'email': '13119144223',
        'password': '123456'
    }
    data = parse.urlencode(data)

    req = request.Request(url, data.encode())

    rsp = opener.open(req)

    #save cookie
    cookie.save(ignore_discard=True, ignore_expire=True)

'''
get profile page
'''
def getHomePage():
    url = 'http://www.renren.com/965187997/profile'

    rsp = opener.open(url)

    html = rsp.read().decode()

    with open('renren.html', 'w') as f:
        f.write(html)


if __name__ == '__main__':
    
    #login()
    #print(cookie)
    #getHomePage()

    cookie.load('cookie.txt', ignore_discard=True)


