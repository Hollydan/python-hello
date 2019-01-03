
from lxml import etree

text = '''
    <div>
        <ul>
            <li class='item-0'><a href='1.html'>1</a></li>
            <li class='item-1'><a href='1.html'>2</a></li>
            <li class='item-2'><a href='1.html'>3</a></li>
            <li class='item-3'><a href='1.html'>4</a></li>
            <li class='item-4'><a href='1.html'>5</a>
        </ul>
    </div>
'''

'''
html = etree.HTML(text)
s = etree.tostring(html)
print(s)
'''

'''
#read xml
html1 = etree.parse('./test.xml')
rst1 = etree.tostring(html1, pretty_print=True)
print(rst1)
'''

#etree and xpath
html = etree.parse('./test.xml')
rst = html.xpath('//book')
print(rst)

print(html.xpath("//book[@category='python']/title"))

