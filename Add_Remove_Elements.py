from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random

service = Service('../chromedriver_mac64/chromedriver')
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for i in range(20):
  driver.find_element(By.XPATH, '//*[@id="content"]/div/button').click()
  time.sleep(random.random() * 1)


try:
  delete_btn = driver.find_element(By.XPATH, '//*[@id="elements"]/child::*')
  while(delete_btn):
    driver.find_element(By.XPATH, '//*[@id="elements"]/child::*').click()
    time.sleep(random.random() * 1)

except:
  print("Completed")