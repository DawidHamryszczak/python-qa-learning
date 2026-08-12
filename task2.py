from selenium.webdriver.common.by import By # POZWALA SZUKAC PO CZYMŚ (LOGICZNE Z NAG SZUKAJ BY IMIE NP)
from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get("https://the-internet.herokuapp.com/")

my_button = driver.find_element(By.LINK_TEXT, "Form Authentication") #TWORZE JAKIS OBIEKT MYBUTTON (PRZYCISK KTORY CHCE WCISNAC) I MOWIE MYBUTTON TO PRZYCISK Z TKESTEM FORM... , MOJ DRIVER GO SZUKA
my_button.click() # KAZE KLIKNAC METODA CLICK - METODA WIEC () NA KONCU
time.sleep(3)

driver.quit()