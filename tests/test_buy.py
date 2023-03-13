import allure
from selenium import webdriver
from base.base_class import Base
from pages.main_page import MainPage
from pages.tv_page import TvPage
from pages.selected_product_page import SelProPage
from pages.basket_page import BasketPage
from utilities.logger import Logger


@allure.description("Test buy TV")
def test_buy_tv() -> None:
    Logger.add_start_step(method="test_buy_tv")
    driver = webdriver.Chrome(
        executable_path='C:\\PycharmProjects\\FinalTestTask\\utilities\\chromedriver.exe')
    base = Base(driver)
    base.open_main_page()
    mp = MainPage(driver)
    mp.move_to_tv_tab()
    tvp = TvPage(driver)
    tvp.full_brand_selection()
    tvp.full_price_selection()
    tvp.full_all_filters_selection()
    tvp.click_select_our_tv()
    spp = SelProPage(driver)
    spp.combine_add_and_move_to_basket()
    bp = BasketPage(driver)
    bp.combine_assert_name_and_price()
    Logger.add_end_step(method="test_buy_tv")
    driver.quit()