from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.base_class import Base


class ProductsPage(Base):
    """Создаем функцию для поиска товара на сайте, используем фильтры
        и добавлением его в корзину в корзину"""

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # Locators

    burger_menu_books = '/html/body/div[1]/div[10]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[1]/span/a'
    comics_manga_artbooks = '//*[@id="header-genres"]/div/ul/li[6]/span'
    manga = '//*[@id="header-genres"]/div/ul/li[6]/ul/li[7]/a'
    main_word = 'genre-name'
    button_all_filters = '//*[@id="catalog-navigation"]/div/form/div[1]/div[1]/div/div/span[4]/span/span/span/span'
    price_filter = '//div[contains(@class, "price-search")]'
    price_filter_min = '//input[@id="section-search-form-price_min"]'
    price_filter_max = '//input[@id="section-search-form-price_max"]'
    publisher_filter = '//div[contains(@class, "block-pubhouse-bl-name")]'
    select_publisher = '//*[@id="section-search-form"]/div[5]/div[2]/div[1]/div/div[2]/div[2]/div/div[3]/label/span[1]'
    cover_filter = '//*[@id="section-search-form"]/div[7]/div[1]'
    select_cover = '/html/body/div[1]/div[10]/div[4]/div[1]/div[8]/div[2]/div/div[4]/div/div[1]/div[4]/div[2]/form/div[7]/div[2]/div[1]/label'
    button_filtered_products = '//input[@class="show-goods__button"]'
    select_product = 'Гангста. Gangsta. Том 1'
    button_add_in_cart = '//*[@id="buyingbtns893397"]/a'

    # Getters

    def get_burger_menu_books(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.XPATH, self.burger_menu_books)))

    def get_burger_menu_comics(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.XPATH, self.comics_manga_artbooks)))

    def get_burger_menu_manga(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.XPATH, self.manga)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.CLASS_NAME, self.main_word)))

    def get_all_filters(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.XPATH, self.button_all_filters)))

    def get_price_filter(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.XPATH, self.price_filter)))

    def get_price_filter_min(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.XPATH, self.price_filter_min)))

    def get_price_filter_max(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.XPATH, self.price_filter_max)))

    def get_publisher_filter(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.XPATH, self.publisher_filter)))

    def get_select_publisher(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.XPATH, self.select_publisher)))

    def get_cover_filter(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.XPATH, self.cover_filter)))

    def get_select_cover(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.XPATH, self.select_cover)))

    def get_button_show_filtered_products(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.XPATH, self.button_filtered_products)))

    def get_select_product(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.LINK_TEXT, self.select_product)))

    def get_button_add_in_cart(self):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.XPATH, self.button_add_in_cart)))

    # Actions

    def click_burger_menu_books(self):
        ActionChains(self.driver).move_to_element(self.get_burger_menu_books()).perform()

    def click_burger_menu_comics(self):
        ActionChains(self.driver).move_to_element(self.get_burger_menu_comics()).perform()

    def click_burger_menu_manga(self):
        self.get_burger_menu_manga().click()
        print('Click burger menu "manga"')

    def click_button_all_filters(self):
        ActionChains(self.driver).move_to_element(self.get_all_filters()).perform()
        self.get_all_filters().click()
        print('Click button All filters')

    def click_price_filter(self):
        ActionChains(self.driver).move_to_element(self.get_price_filter()).perform()
        self.get_price_filter().click()
        print('Click price filter')

    def change_price_filter_min(self, price_filter_min):
        self.get_price_filter_min().send_keys(price_filter_min)
        print('Input min price')

    def change_price_filter_max(self, price_filter_max):
        self.get_price_filter_max().send_keys(price_filter_max)
        print('Input max price')

    def click_publisher_filter(self):
        ActionChains(self.driver).move_to_element(self.get_publisher_filter()).perform()
        self.driver.execute_script("arguments[0].click();", self.get_publisher_filter())
        print('Click publisher filter')

    def click_publisher(self):
        ActionChains(self.driver).move_to_element(self.get_select_publisher()).perform()
        self.driver.execute_script("arguments[0].click();", self.get_select_publisher())
        print('Select publisher')

    def click_cover_filter(self):
        ActionChains(self.driver).move_to_element(self.get_cover_filter()).perform()
        self.driver.execute_script("arguments[0].click();", self.get_cover_filter())
        print('Click cover filter')

    def click_select_cover(self):
        ActionChains(self.driver).move_to_element(self.get_select_cover()).perform()
        self.driver.execute_script("arguments[0].click();", self.get_select_cover())
        print('Select cover')

    def click_button_show_filtered_products(self):
        self.get_button_show_filtered_products().click()
        print('Print button show filtered products')

    def click_select_product(self):
        ActionChains(self.driver).move_to_element(self.get_select_product()).perform()
        self.driver.execute_script("arguments[0].click();", self.get_select_product())
        print('Select product')

    def click_button_add_in_cart(self):
        self.get_button_add_in_cart().click()
        print('Click button Add in cart')

    # Methods

    def select_products(self):
        self.click_burger_menu_books()
        self.click_burger_menu_comics()
        self.click_burger_menu_manga()
        self.get_current_url()
        self.assert_word(self.get_main_word(), 'Манга')
        self.click_button_all_filters()
        self.click_price_filter()
        self.change_price_filter_min('500')
        self.change_price_filter_max('2000')
        self.click_publisher_filter()
        self.click_publisher()
        self.click_cover_filter()
        self.click_select_cover()
        self.click_button_show_filtered_products()
        self.click_select_product()
        self.click_button_add_in_cart()
