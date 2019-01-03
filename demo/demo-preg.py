
import re

'''
s = r'\d+'

pattern = re.cpmpile(s)

m = pattern.match('7483hfusdhfjdbv874')
print(m)

#offset
m = pattern.match('7483hfusdhfjdbv874', 5, 10)
print(m)
print(m.group())
print(m.start(0))
print(m.end(0))
print(m.span(0))
'''

s = r'([a-z]+) ([a-z]+)'

pattern = re.compile(s, re.I)

m = pattern.match('Hello world wide web')

print(m.group(0))
print(m.span(0))
print(m.group(1))
print(m.span(0))

print(m.groups())

res = pattern.search('hello world wide web')

res1 = pattern.findall('hello world')
res2 = pattern.finditer('hello world')
res3 = pattern.split('hello world')
res4 = pattern.sub('hello world', ',')

#unicode
ss = r'[\u4e00-\u9fa5]'

