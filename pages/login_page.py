from selenium.webdriver.common.by import By

class LoginPage:

    #1 Konstuktor - przyjmuje drivera i go zapsiuje w obiekcie, ustawia url strony logowania oraz lokatory elementów na stronie 
    #  Klasyk aby mozna bylo z tego korzystac w calej klasie 
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/login"

        #lokatorzy (adresy elementów na stronie)
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.TAG_NAME, "button")
        self.flash_message = (By.ID, "flash")

    #2 AKCJE NA STORNIE 

    #Otwieram strone przez get i zmienna self.url pod ktora kryje sie adres strony logowania
    def open(self):
        self.driver.get(self.url)

    #Funckja logowania przyjmuje login i haslo jako parametry, znajduje elementy na stronie przez elementy w kotrych zapisane sa adresy elementow strony 
    # Wpisuje do nich dane, a następnie klika przycisk logowania, lokalizujac go rowniez przez zmienne z konstruktora
    def login(self, login, password):
        self.driver.find_element(*self.username_input).send_keys(login)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    #Funkcja pobierajaca tekst z elementu strony, szuka go poprzez element z konstruktora self.flash_message i zwraca jego tekst
    def get_flash_message(self):
        return self.driver.find_element(*self.flash_message).text     
      