from selenium import webdriver
from pages.dropdown_page import DropdownPage

def test_select_dropdown_option(driver):
    dropdown_page = DropdownPage(driver)
    dropdown_page.open()
   
    dropdown_page.select_option_by_text("Option 2")
    assert "Option 2" in dropdown_page.get_selected_option_text()

def test_select_dropdown_by_index(driver):
    dropdown_page = DropdownPage(driver)
    dropdown_page.open()

    dropdown_page.select_option_by_index(2)
    assert "Option 2" in dropdown_page.get_selected_option_text()    
