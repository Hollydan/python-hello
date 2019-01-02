import os
import time

#source = [r'e:\python']
source = ["e:\\python"]

target_dir = "e:\\python\\backup"

target = target_dir + os.sep +\
        time.strftime('%Y%m%d%H%M%S') + '.zip'

#print(source, targe)
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = 'zip -r {} {}'.format(target, ''.join(source))

#print(zip_command)
if os.system(zip_command) == 0:
    print('successful')
else:
    print('false')
