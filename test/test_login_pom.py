from selenium import webdriver
from pages.login_page import LoginPage

def test_successful_login(driver):

    #STWORZENIE ELEMENTU login_page POD KTORYM KRYJE SIE KLASA LoginPage
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    assert "You logged into a secure area!" in login_page.get_flash_message()

def test_invalid_login(driver):

    #STWORZENIE ELEMENTU login_page POD KTORYM KRYJE SIE KLASA LoginPage
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("invalid_user", "invalid_password")
    login_page.get_flash_message()

    assert "Your username is invalid!" in login_page.get_flash_message()