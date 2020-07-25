



email='siginamsettyphani@gmail.com'
password='1681149@sP'







from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import clipboard
import time 
import os


repo=input('enter repository name: ')

driver=webdriver.Chrome('chromedriver.exe')

driver.get('https://github.com/login')

user=driver.find_element_by_id('login_field')
user.send_keys(email)

user=driver.find_element_by_id('password')
user.send_keys(password)


signin=driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')

signin.submit()


new=driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a')
new.click()

time.sleep(8)

new=driver.find_element_by_xpath('//*[@id="repository_name"]')
new.send_keys(repo)


check=driver.find_element_by_xpath('//*[@id="repository_auto_init"]')
check.click()


create=driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')
create.submit()

time.sleep(8)


clone =driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div/div[2]/div[1]/div[2]/span/get-repo/details/summary')
clone.click()


clone =driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div/div[2]/div[1]/div[2]/span/get-repo/details/div/div/div[1]/div/div[1]/div/div/clipboard-copy')
clone.click()


giturl=clipboard.paste()
print(giturl)


os.system('git init')

os.system('git add .')

os.system('git status')

os.system('git commit -m "Initial commit"')

os.system('git remote add origin '+giturl)

os.system('git push -f origin master')


print('\n  Task Completed...!')



























