from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.base_class import Base


class CartPage(Base):
    """Создаем функцию для работы с товаром в корзине,
        без оформления товара."""

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # Locators

    button_cart = '//*[@id="minwidth"]/div[6]/div/div[1]/div[2]/div/ul/li[6]/a'
    name_product_word = 'product-title'
    big_red_button = '//button[contains(@class, "btn-primary")]'

    # Getters

    def get_button_cart(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.XPATH, self.button_cart)))

    def get_name_product_word(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.CLASS_NAME, self.name_product_word)))

    def get_big_red_button(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.XPATH, self.big_red_button)))

    # Actions

    def click_button_cart(self):
        self.get_button_cart().click()
        print('Click button Cart')

    def click_big_red_button(self):
        self.get_big_red_button().click()
        print('Click Big red button')

    # Methods

    def buy_products(self):
        self.click_button_cart()
        self.assert_word(self.get_name_product_word(), 'Гангста. Gangsta. Том 1')
        self.click_big_red_button()
