from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By as by
import time

service = Service("./chromedriver_mac64/chromedriver")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.maximize_window()
driver.get("https://www.youtube.com/")

search = driver.find_element(by.XPATH, '//input[@id="search"]')
search.send_keys("slander love is gone")
time.sleep(1)

driver.find_element(by.XPATH, '//button[@id="search-icon-legacy"]').click()
time.sleep(3)

driver.find_element(by.XPATH, '//yt-formatted-string[contains(text(), "SLANDER - Love Is Gone ft. Dylan Matthew (Acoustic)")]').click()



