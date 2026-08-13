from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class CheckboxPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/checkboxes"

        self.check_box = (By.XPATH, "//form[@id='checkboxes']/input[1]")

    def open(self):
        self.driver.get(self.url)

    def click_first_checkbox(self):
        first_checkbox = self.driver.find_element(*self.check_box).click()

    def is_fist_checkbox_selected(self):
        first_checkbox = self.driver.find_element(*self.check_box)
        return first_checkbox.is_selected()

    