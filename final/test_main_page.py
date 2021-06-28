import pytest
from .pages.main_page import MainPage


class TestMainPage:
    link = "http://selenium1py.pythonanywhere.com/en-gb/"

    @pytest.mark.parametrize('lang', [pytest.param("en-gb/", marks=pytest.mark.xfail), "ru/", "es/", "fr/"])
    def test_add_to_cart_basket_btn_is_not_presented_on_main_page(self, browser, lang):
        # Arrange
        link = f"http://selenium1py.pythonanywhere.com/{lang}"
        main_page = MainPage(browser, link)
        main_page.open()
        # Act
        main_page.scroll_page_down()
        # Assert
        main_page.should_not_be_add_to_basket_btn()

    def test_welcome_text_presented_on_main_page(self, browser):
        # Arrange
        main_page = MainPage(browser, self.link)
        #Act
        main_page.open()
        # Assert
        main_page.should_be_welcome_text()

