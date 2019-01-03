
from urllib import request
from bs4 import Beautifuloup

url = 'http://www.baidu.com'

rsp = request.urlopen(url)

content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

content = soup.prettify()

#print(content)
'''
print(soup.head)
print('==' * 12)
print(soup.meta)
print('--' * 12)
print(soup.link)

print(soup.link.name)
print(soup.link.attrs['type'])

soup.link.attrs['type'] = 'hhh'
print(soup.link.attrs)
'''
'''
print(soup.title)
print(soup.title.string)

print(soup.name)
'''
'''
for node in soup.head.contents:
    if node.name == 'meta':
        print(node)
    if node.name == 'title':
        print(node.string)
'''

'''
tags = soup.find_all(name='meta')
print(tags)
'''
titles = soup.select('title')
print(titles[0])

metas = soup.select("meta[content='always']")
print(metas[0])






