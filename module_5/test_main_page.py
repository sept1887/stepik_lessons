import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        # Arrange
        main_page = MainPage(browser, link)
        main_page.open()
        # Act
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        # Assert
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        # Arrange
        main_page = MainPage(browser, link)
        # Act
        main_page.open()
        # Assert
        main_page.should_be_login_link()


@pytest.mark.basket_guest
class TestBasketFromMainPage:
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # Arrange
        main_page = MainPage(browser, link)
        main_page.open()
        # Act
        main_page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        # Assert
        basket_page.should_not_be_items_in_basket()
        basket_page.should_be_empty_basket_msg()
