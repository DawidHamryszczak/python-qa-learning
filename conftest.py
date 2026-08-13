import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options

@pytest.fixture
def driver():
    #STWORZENIE SETUPU DLA PRZEGLADARKI, ZEBY TESTY DZIALALY W TLE
    options = Options()
    options.add_argument("--headless")  # Uruchomienie przeglądarki w trybie headless (bez interfejsu graficznego)  
    #STWORZENIE SETUPU KTORY ZAWSZE ZROBI SIE PRZED TESTEM ZEBY NIE PISAC TEGO 10000 RAZY
    browser = webdriver.Edge(options=options)
    browser.implicitly_wait(10)  # Czekaj maksymalnie 10 sekund na zaladowanie elementu

    yield browser #Przekazanie obiektu browser do testu, wszytsko powyzej dzieje sie przed testem, wszystko ponizej dzieje sie po teście

    browser.quit() #Zamkniecie przegladarki po zakonczeniu testu