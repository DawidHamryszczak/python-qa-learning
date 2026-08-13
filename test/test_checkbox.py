from selenium import webdriver
from pages.checkbox_page import CheckboxPage

def test_select_first_checkbox(driver):
    checkbox_page = CheckboxPage(driver)
    checkbox_page.open()
    checkbox_page.click_first_checkbox()
    

    assert checkbox_page.is_fist_checkbox_selected() is True
