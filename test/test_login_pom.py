from selenium import webdriver
from pages.login_page import LoginPage

def test_successful_login():

    #STWORZENIE DRIVERA
    driver = webdriver.Edge()
    #STWORZENIE ELEMENTU login_page POD KTORYM KRYJE SIE KLASA LoginPage
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    message_text = login_page.get_flash_message()

    assert "You logged into a secure area!" in message_text