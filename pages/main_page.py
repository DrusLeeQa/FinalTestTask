from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    TVs = "//*[contains(text(),'Телевизоры')]"

    # Getters

    def get_tvs(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.TVs)))

    # Actions

    def click_tvs(self):
        self.get_tvs().click()
        print("Select TVs")

    # Methods

    def select_tvs(self):
        self.get_current_url()
        self.click_tvs()