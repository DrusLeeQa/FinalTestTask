from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import ActionChains, Keys


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    search_mp = "//input[@id='searchInput']"

    # Getters

    def get_search(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.search_mp)))

    # Actions

    def input_in_search(self, value):
        self.get_search().send_keys(value, Keys.RETURN)

    # Methods

    def move_to_tv_tab(self):
        self.get_current_url()
        self.input_in_search("Телевизоры")
