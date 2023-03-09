import time

from selenium import webdriver
from base.base_class import Base
from pages.main_page import MainPage
from pages.tv_page import TvPage


def test_buy() -> None:
    sleep = 1
    driver = webdriver.Chrome(
        executable_path='C:\\PycharmProjects\\FinalTestTask\\utilities\\chromedriver.exe')
    base = Base(driver)
    base.open_main_page()
    time.sleep(sleep)
    mp = MainPage(driver)
    mp.move_to_tv_tab()
    time.sleep(sleep)
    tvp = TvPage(driver)
    tvp.full_brand_selection()
    tvp.full_price_selection()
    tvp.full_all_filters_selection()
    tvp.click_select_our_tv()
    time.sleep(sleep)

