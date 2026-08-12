#1 STWORZENIE FUKNCJI Z PARAMETREM TEST_NAME, KTORA DRUKUJE TEKST
def make_ss(test_name):
    print("ScreenShoot for test:", test_name)
    print("Saved as:", test_name + ".png")

#2 STWORZENIE KLASY
class LoginPage:

    #STWORZENIE METODY (INACZEJ FUNKCJI W KLASIE) - w FUNKCJI STWORZENEJ KLASIE, ZAWWSZE PIERWSZY PARAMETR TO SELF - CZYLI FUNKCJA ODWOLUJE SIE DO SIEBIE
    def open_page(self):
        print("Open page in browser: www.gmail.com/login")

    def insert_data(self, login, password):
        print("Insert login:", login)
        print("Insert password:", password)

    def click_login(self):
        print("Click login button")

#UZYCIE FUNKCJI I METOD
print("--START TEST--")

login_panel = LoginPage() # PRZYPISUJEMY NASZA KLASE DO ZMIENNEJ - ROBIMY Z NIEJ ZYWY OBIEKT

login_panel.open_page()
login_panel.insert_data("tomsmith", "qwerty123")
login_panel.click_login()

make_ss("login_test")

print("--FINISHED TEST--")