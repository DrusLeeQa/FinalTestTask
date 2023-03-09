import time

import pytest
from selenium import webdriver
from base.base_class import Base
from pages.main_page import MainPage
from pages.tv_page import TvPage


def test_buy() -> None:
    driver = webdriver.Chrome(
        executable_path='C:\\PycharmProjects\\FinalTestTask\\utilities\\chromedriver.exe')
    base = Base(driver)
    base.open_main_page()
    time.sleep(3)
    mp = MainPage(driver)
    mp.move_to_tv_tab()
    time.sleep(5)
    tvp = TvPage(driver)
    tvp.full_brand_selection()

