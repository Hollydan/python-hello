
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

'''
driver = webdriver.PhantomJS()

driver.get('http://www.baidu.com')

print('title: {}'.format(driver.title))
'''

driver = webdriver.Chrome()

url = 'http://www.baidu.com'

driver.get(url)

text = driver.find_element_by_id('wrapper').text
print(text)

driver.save_screenshot('baidu.png')

#input python
driver.find_element_by_id('kw').send_keys('python')

#click search
driver.find_element_by_id('su').click()

time.sleep(5)
driver.save_screenshot('python-search.png')

#get cookie
print(driver.get_cookies())

#input ctrl + a
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
#input ctrl + x
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

driver.find_element_by_id('kw').send_keys('php')
driver.find_element_by_id('su').send_keys(Keys.RETURN)
time.sleep(5)
driver.save_screenshot('php-search.png')

#clear kw
driver.find_element_by_id('kw').clear()
driver.save_screenshot('clear.png')

#close brower
driver.quit()


