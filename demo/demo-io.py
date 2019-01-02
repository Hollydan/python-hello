
"""
def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input('enter text: ')

if is_palindrome(something):
    print('ok')
else:
    print('no')
"""

poem = '''\
    Programming is fun
    When the work is done
    if you wanna make your work also fun:
    use Python!
    '''

f = open('python-hello.txt', 'w')
f.write(poem)
f.close()

f = open('python-hello.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)

f.close()
