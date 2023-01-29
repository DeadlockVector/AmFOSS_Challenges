#import re
import time, sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains

#emailRegex = re.compile(r'([a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))')

#setting up driver, action objects
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
action = ActionChains(driver)

#opening gmail
driver.get("https://www.google.com/intl/en-GB/gmail/about/")
time.sleep(1)

#signing in to gmail
signin_button = driver.find_element(By.XPATH, '/html/body/header/div/div/div/a[2]')
action.click(on_element = signin_button).perform()
time.sleep(2)

#entering email id
email_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
email_element.send_keys("seleniumJackson2004@gmail.com")
next_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
action.click(on_element = next_button).perform()
time.sleep(2)
#entering password
password_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
password_element.send_keys("seleniumtesting2004#$@")
next1_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[3]')
action.click(on_element = next1_button).perform()
time.sleep(2)

#composing mail
compose_button = driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div')
action.click(on_element = compose_button).perform()
time.sleep(2)
send_email = driver.find_element(By.XPATH, '/html/body/div[28]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[1]/td[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/input')
send_email.send_keys(sys.argv[1])
time.sleep(10)
'''
message = ""
try:
    for i in range(2, len(sys.argv)+2):
        message += i
    print(message)
except:
    print("Enter email address and message in that order")
'''

