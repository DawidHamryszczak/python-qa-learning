from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get("https://the-internet.herokuapp.com/login")   

user_field = driver.find_element(By.ID, "username")
user_field.send_keys("tomsmith") #FUNKCJA SEND_KEYS WPISUJE TWOJ TEKST W POLE

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!") #FUNKCJA SEND_KEYS WPISUJE TWOJ TEKST W POLE

login_button = driver.find_element(By.TAG_NAME, "button")
login_button.click()

time.sleep(3)
driver.quit()
