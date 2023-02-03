import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
action = ActionChains(driver)

driver.get("https://gabrielecirulli.github.io/2048/")
time.sleep(5)

toSendControls = driver.find_element(By.TAG_NAME, 'html')

while True:
    toSendControls.send_keys(Keys.UP)
    toSendControls.send_keys(Keys.RIGHT)
    toSendControls.send_keys(Keys.DOWN)
    toSendControls.send_keys(Keys.LEFT)
