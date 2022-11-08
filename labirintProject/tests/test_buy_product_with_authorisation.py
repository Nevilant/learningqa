import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_buy_product():
    """Собираем тест"""

    s = Service('/home/nevi/Документы/resource/chromedriver')
    driver = webdriver.Chrome(service=s)

    mp = MainPage(driver)
    mp.go_to_site()

    login = LoginPage(driver)
    login.authorisation()

    pg = ProductsPage(driver)
    pg.select_products()

    cp = CartPage(driver)
    cp.buy_products()

    time.sleep(5)
