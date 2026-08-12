from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get("https://www.wikipedia.org/")
time.sleep(3)

driver.quit()