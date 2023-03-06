import time

import pytest
from selenium import webdriver
from base.base_class import Base
from pages.main_page import MainPage
from pages.tv_page import TvPage


def test_buy_tv_lg() -> None:
    driver = webdriver.Chrome(
        executable_path='C:\\PycharmProjects\\FinalTestTask\\utilities\\chromedriver.exe')
    base = Base(driver)
    base.open_main_page()
    time.sleep(2)
    tv = TvPage(driver)
    tv.select_tvs()
    time.sleep(2)


