from selenium import webdriver
from selenium.webdriver.common.by import By
#FUNNKCJA TEST LOGOWANIA
def test_login():
    #STWORZENIE OBIEKTU DRIVER KTORY BEDZIE STEROWAL PRZEGLADARKA EDGE
    driver = webdriver.Edge()
    #OTWORZENIE STRONY LOGOWANIA
    driver.get("https://the-internet.herokuapp.com/login")

    #ZNAJDZ ELEMENT PO ID USERNAME I WPISZ TOMSMITH
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    #ZNAJDZ ELEMENT PO ID PASSWORD I WPISZ SUPERSECRETPASSWORD!
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    #ZNAJDZ ELEMENT PO TAGU BUTTON I KLIKNIJ GO
    driver.find_element(By.TAG_NAME, "button").click()

    #ZNAJDZ ELEMENT PO ID FLASH I PRZYPISZ JEGO TEKST DO OBIEKTU TEXT
    text = driver.find_element(By.ID, "flash").text
    driver.quit()
    #sprawdzenie czy w obiekcie text znajdują się słowa "You logged into a secure area!"
    assert "You logged into a secure area!" in text
