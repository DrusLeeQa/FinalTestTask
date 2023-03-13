import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class SelProPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Service variables

    # Locators

    selected_product_price = "(//ins[@class='price-block__final-price'])[2]"
    selected_product_name = "//h1[@data-link='text{:selectedNomenclature^goodsName || product^goodsName}']"
    add_to_basket = "(//span[text()='Добавить в корзину'])[2]"
    move_to_basket = "(//a[text()='        Перейти в корзину    '])[2]"

    # Getters

    def get_selected_product_price(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.selected_product_price)))

    def get_selected_product_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.selected_product_name)))

    def get_add_to_basket(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_basket)))

    def get_move_to_basket(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.move_to_basket)))

    # Actions

    def click_add_to_basket(self):
        self.get_add_to_basket().click()
        print("Click add to basket")

    def click_move_to_basket(self):
        self.get_move_to_basket().click()
        print("Click move to basket")

    # Methods

    def combine_add_and_move_to_basket(self):
        with allure.step("Combine add and move to basket"):
            Logger.add_start_step(method="combine_add_and_move_to_basket")
            Base.spp_name = self.get_selected_product_name().text
            Base.spp_price = self.get_selected_product_price().text
            self.click_add_to_basket()
            self.click_move_to_basket()
            self.get_current_url()
            time.sleep(1.5)
            self.get_screenshot("bp")
            Logger.add_end_step(method="combine_add_and_move_to_basket")