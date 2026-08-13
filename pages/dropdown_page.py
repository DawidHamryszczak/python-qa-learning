from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class DropdownPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/dropdown"

        #lokatorzy (adresy elementów na stronie)
        self.dropdown = (By.ID, "dropdown")

    def open(self):
        self.driver.get(self.url)

    def select_option_by_text(self, text):
        select_object = Select(self.driver.find_element(*self.dropdown))
        #PRZEKAZUJEMY ELEMENT DO KLASY SELECT
        
        select_object.select_by_visible_text(text)

    def get_selected_option_text(self):
        select_object = Select(self.driver.find_element(*self.dropdown))
        return select_object.first_selected_option.text
    
    def select_option_by_index(self, index):
        select_object = Select(self.driver.find_element(*self.dropdown))
        select_object.select_by_index(index)
