from selenium.webdriver.common.by import By

class InputsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/inputs"

        self.input = (By.TAG_NAME, "input")

    def open(self):
        self.driver.get(self.url)

    def enter_number(self, number):
        self.driver.find_element(*self.input).send_keys(str(number))

    def get_input_values(self):
        return self.driver.find_element(*self.input).get_attribute("value")    
        



