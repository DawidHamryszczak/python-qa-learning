from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver  = webdriver.Edge()
driver.get("https://the-internet.herokuapp.com/login") #OTWORZ TA STRONE

driver.find_element(By.ID, "username").send_keys("tomsmith") #ZNAJDZ ELEMENT PRZEZ ID USERNAME I WPISZ TOMSMITH
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!") #ZNAJDZ ELEMENT PRZEZ ID PASSWORD I WPISZ SUPERSECRETPASSWORD!

driver.find_element(By.TAG_NAME, "button").click() #ZNAJDZ ELEMENT PO TAGNAME BUTTON (CZYLI BEDZIE TO PRZYCISK) I KLIKNIJ TO

message = driver.find_element(By.ID, "flash") #ZNAJDZ ELEMENT PO ID FLASH I JEST TO OBIEKT MESSAGE (TEN OBIEKT TO POWIADOMIENIE CZY UDALO SIE ZALGOOWAC CZY NIE) 
#(BY FLASH BO TAKIE ID MAJA NA TEJ STORNIE CHWILOWE POWIADOMIENIA, ERRORY ITP)
text = message.text #STWORZONO OBIEKT TEXT I PRZYPISANO DO NIEGO TEKST KTORY ZNADUJE SIE W ELEMENCIE MESSAGE

print("TEXT FROM PAGE:", text) #WYPISZ OBIEKT TEXT CZYLI TO CO ZNALEZLES W MESSAGE NA STRONIE

assert "You logged into a secure area!" in text, "BŁĄD: Logowanie nie powiodło się" #SPRAWDZ CZY SA SLOWA YOU LOGGED... ALBO SLOWA BŁĄD.... W OBIKECIE TEXT

print("LOGIN SUCCESSFULLY") #JESLI SA SŁOWA LOGGED... WYDRKUJ ZE SUKCES JESLI SA BŁĄD... TO WYWALI BŁĄD

time.sleep(3) #ZAMRAZAM CZAS NA 3 SEKUNDY ZEBYM MOGL SAM ZOBACZYC JAK TO SIE DZIEJE
driver.quit()