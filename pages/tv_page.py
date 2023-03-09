import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import ActionChains, Keys


class TvPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    open_brand_filter = "(//button[@class='dropdown-filter__btn'])[2]"
    show_all = "//button[@class='filter__show-all j-show-whole-filters']"
    search_brand = "//input[@class='j-search-filter']"
    select_xiaomi = "//span[text()='Xiaomi']"
    ready = "//*[contains(text(), 'Готово')]"

    # Getters

    def get_open_brand_filter(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.open_brand_filter)))

    def get_show_all(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.show_all)))

    def get_search_brand(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.search_brand)))

    def get_select_xiaomi(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.select_xiaomi)))

    def get_ready(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ready)))

    # Actions

    def click_open_brand_filter(self):
        self.get_open_brand_filter().click()
        print("Click open brand filter")

    def click_show_all(self):
        self.get_show_all().click()
        print("Click show all")

    def input_brand_in_search(self, value):
        self.get_search_brand().send_keys(value)
        print("Entered the value of the brand in the search and pressed enter")

    def click_select_xiaomi(self):
        self.get_select_xiaomi().click()
        print("Сhose xiaomi among the found")

    def click_ready(self):
        self.get_ready().click()
        print("Click ready")

    # Methods

    def full_brand_selection(self):
        self.click_open_brand_filter()
        time.sleep(3)
        self.click_show_all()
        time.sleep(3)
        self.input_brand_in_search("Xiaomi")
        time.sleep(3)
        self.click_select_xiaomi()
        time.sleep(3)
        self.click_ready()
        time.sleep(5)