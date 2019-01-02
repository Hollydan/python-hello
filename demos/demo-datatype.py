import sys

'''for i in sys.argv:
    print(i)
print(sys.path)'''

'''if __name__ == '__main__':
    print('this program is being run by itself')
else:
    print('i am being imported by another module')'''

'''a = 5
print(dir())
#print(dir(sys))'''

'''shop_list = ['apple', 'mangs', 'carrot', 'banana']

print(len(shop_list))
print('this item are:', end='')
for item in shop_list:
    print(item, end=',')

print('i also have to buy rice')
shop_list.append('rice')
print('my shop list is now', shop_list)

print('i will sort my list now')
shop_list.sort()
print('sorted shop list is now', shop_list)

olditem = shop_list[0]
del shop_list[0]
print('I bought the', olditem)
print('my shop list is now', shop_list)'''

'''zoo = ('python', 'elephant', 'penguin')
print('number of animials in the zoo is ', len(zoo))

new_zoo = ('monkey', 'camel', zoo)
print('number of cages in the new zoo is ', len(new_zoo))

print('all animals in new zoo are ', new_zoo)
print('animals brought from old zoo are ', new_zoo[2])'''

'''ab = {
    'zs': 'zs.com',
    'ls': 'ls.com',
    'ww': 'ww.org'
}
print('zs address is ', ab['zs'])

del(ab['zs'])
print('there are {} address in the ab'.format(len(ab)))

for name, address in ab.items():
    print('{} address is {}'.format(name, address))

ab['guido'] = 'guido.org'
if 'guido' in ab:
    print('guido address is ', ab['guido'])'''

'''bri = set(['zhang', 'wang', 'zhao', 'lee'])
print('lee' in bri)

bric = bri.copy()
bric.add('ren')
print(bric.issuperset(bri))

bri.remove('zhang')
print(bri & bric)'''

name = 'swaroop'
if name.startswith('swa'):
    print('yes')

if 'oo' in name:
    print('yes')

if name.find('war') != -1:
    print('yes')

delimiter = '_*_'
print(delimiter.join(name))




