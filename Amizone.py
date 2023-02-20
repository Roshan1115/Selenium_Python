from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

print("Heyy")


path = "./chromedriver_mac64/chromedriver"
service_obj = Service(path)
Driver = webdriver.Chrome(service=service_obj, chrome_options=chrome_options)

Driver.get("https://s.amizone.net/")

print(Driver.title)


bar = Driver.find_element(By.XPATH, '//*[@id="loginform"]/div[1]/input[1]')
bar.send_keys("8426066")



bar2 = Driver.find_element(By.XPATH, '//*[@id="loginform"]/div[2]/input')
bar2.send_keys("4558ff")


Driver.find_element(By.XPATH, '//*[@id="loginform"]/div[4]/button').click()

time.sleep(10)
Driver.find_element(By.XPATH, '//*[@id="myModalVacc"]/div/div/div[1]/button').click()
Driver.find_element(By.XPATH, '//*[@id="ModalPopAppAyf"]/div/div/div[1]/button').click()



