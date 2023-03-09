import datetime
from selenium.webdriver import ActionChains


class Base:
    url = "https://www.wildberries.ru/"

    def __init__(self, driver):
        self.driver = driver

    """Method that opens browser"""

    def open_main_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        print("\nOpen Browser")

    """Method that gets the current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url {get_url}")

    """Method that asserts the word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method for taking screenshots"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%d.%m.%Y")
        name_screenshot = f"screenshot_{now_date}.png"
        self.driver.save_screenshot(
            'C:\\PycharmProjects\\FinalTestTask\\screens\\' + name_screenshot)
        print("Maked a screen")

    """Method that asserts the url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method that scroll page down by a certain value"""

    def scroll_page_down(self, value):
        self.driver.execute_script(f"window.scrollTo(0, {str(value)})")
        print("Scrolled page")

    """Method that scroll page up to a certain element"""

    def move_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
