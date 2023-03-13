from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import allure


class BasketPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Service variables

    # Locators

    basket_product_price = "//div[@class='list-item__price-new']"
    basket_product_name = "//span[@class='good-info__good-name']"
    product_count = "//div[@class='count__wrap']"

    # Getters

    def get_basket_product_price(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.basket_product_price)))

    def get_basket_product_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.basket_product_name)))

    def combine_assert_name_and_price(self):
        with allure.step("Combine assert name and price"):
            assert Base.spp_name == self.get_basket_product_name().text
            print("Names matched")
            assert self.del_two_last(Base.spp_price) == self.del_two_last(self.get_basket_product_price().text)
            print("Prices converged")
