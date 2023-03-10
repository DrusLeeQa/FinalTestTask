import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class TvPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Service variables

    diagonal = '50"'
    sleep = 1

    # Locators

    brand_filter = "(//button[@class='dropdown-filter__btn'])[2]"
    show_all = "//button[@class='filter__show-all j-show-whole-filters']"
    search_brand = "//input[@class='j-search-filter']"
    select_xiaomi = "//span[text()='Xiaomi']"
    ready = "//*[contains(text(), 'Готово')]"
    price_filter = "(//button[@class='dropdown-filter__btn'])[4]"
    start_price = "//input[@name='startN']"
    end_price = "//input[@name='endN']"
    all_filters = "//button[@class='dropdown-filter__btn dropdown-filter__btn--all']"
    diagonal_50 = f"//span[text()='{diagonal}']"
    smart_tv = "//span[text()='Smart TV']"
    wi_fi = "//span[text()='Wi-Fi']"
    show = "//button[text()='Показать']"
    select_our_tv = "//span[text()='Телевизор Mi LED TV 4S 50']"

    # Getters

    def get_brand_filter(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.brand_filter)))

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

    def get_price_filter(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.price_filter)))

    def get_start_price(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.start_price)))

    def get_end_price(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.end_price)))

    def get_all_filters(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.all_filters)))

    def get_diagonal_50(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.diagonal_50)))

    def get_smart_tv(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.smart_tv)))

    def get_wi_fi(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.wi_fi)))

    def get_show(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.show)))

    def get_select_our_tv(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.select_our_tv)))

    # Actions

    def click_brand_filter(self):
        self.get_brand_filter().click()
        print("Click brand filter")

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

    def click_price_filter(self):
        self.get_price_filter().click()
        print("Click price filter")

    def input_start_price(self, value):
        self.get_start_price().clear()
        self.get_start_price().send_keys(value)
        print("Entered starting price")

    def input_end_price(self, value):
        self.get_end_price().clear()
        self.get_end_price().send_keys(value)
        print("Entered ending price")

    def click_all_filters(self):
        self.get_all_filters().click()
        print("Clicked all filters")

    def select_diagonal_50(self):
        self.get_diagonal_50().click()
        print("Selected diagonal 50")

    def select_smart_tv(self):
        self.get_smart_tv().click()
        print("Selected smart tv")

    def select_wi_fi(self):
        self.get_wi_fi().click()
        print("Selected wi-fi")

    def click_show(self):
        self.get_show().click()
        print("Click show")

    def click_select_our_tv(self):
        self.move_to_element(self.get_select_our_tv())
        self.get_select_our_tv().click()
        print("Selected our tv")
        time.sleep(1.5)
        self.get_screenshot("spp")

    # Methods

    def full_brand_selection(self):
        self.click_brand_filter()
        time.sleep(self.sleep)
        self.click_show_all()
        time.sleep(self.sleep)
        self.input_brand_in_search("Xiaomi")
        time.sleep(self.sleep)
        self.click_select_xiaomi()
        time.sleep(self.sleep)
        self.click_ready()
        time.sleep(self.sleep)

    def full_price_selection(self):
        self.click_price_filter()
        time.sleep(self.sleep)
        self.input_start_price(30000)
        time.sleep(self.sleep)
        self.input_end_price(50000)
        time.sleep(self.sleep)
        self.click_ready()
        time.sleep(self.sleep)

    def full_all_filters_selection(self):
        self.click_all_filters()
        time.sleep(self.sleep)
        self.move_to_element(self.get_diagonal_50())
        time.sleep(self.sleep)
        self.select_diagonal_50()
        time.sleep(self.sleep)
        self.move_to_element(self.get_wi_fi())
        time.sleep(self.sleep)
        self.select_smart_tv()
        time.sleep(self.sleep)
        self.select_wi_fi()
        time.sleep(self.sleep)
        self.click_show()