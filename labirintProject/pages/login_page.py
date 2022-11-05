from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.base_class import Base


class LoginPage(Base):
    """Создаем функцию авторизации на сайте"""

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # Locators

    button_cabinet = '//a[contains(@class, "top-link-main_cabinet")]'
    field_user_name = '/html/body/div[1]/div[1]/div/div/div/div/div[1]/form[1]/div[3]/input'
    button_login = '//input[@id="g-recap-0-btn"]'

    # Getters

    def get_button_cabinet(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.XPATH, self.button_cabinet)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.XPATH, self.field_user_name)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.XPATH, self.button_login)))

    # Actions

    def click_button_cabinet(self):
        self.get_button_cabinet().click()
        print('Click cabinet button')

    def input_user_name(self, field_user_name):
        self.get_user_name().send_keys(Keys.CONTROL + 'a')
        self.get_user_name().send_keys(Keys.BACKSPACE)
        self.get_user_name().send_keys(field_user_name)
        print('Input discount code')

    def click_button_login(self):
        self.get_button_login().click()
        print('Click button login')

    # Methods

    def authorisation(self):
        self.click_button_cabinet()
        self.input_user_name('2862-489A-A1B8')
        self.click_button_login()
