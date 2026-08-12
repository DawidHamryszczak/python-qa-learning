#SKRYPT OTWIERAJACY STRONE
from selenium import webdriver
import time

print("Start BOT...")

#TWORZYMY OBIKET PRZEGLADARKI
driver = webdriver.Edge()

#WYDAJEMY POLECENIA
print("I open testing page...")
driver.get("https://the-internet.herokuapp.com/") #GET - POBIERA I LADUJE STRONE

#TUTAJ WYKORZYSTUJEMY TIME ABY ZATRZYMAC CZAS ZEBY WIDZIEC EFEKT
print("Wait 3 seconds...")
time.sleep(3)

#KONCZYMY TEST
print("I close testing page.")
driver.quit()