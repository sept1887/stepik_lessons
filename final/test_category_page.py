import pytest
from .pages.main_page import MainPage
from .pages.category_page import CategoryPage


class TestCategoryPage:
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/category/books_2/"

    def test_should_be_home_page_link(self, browser):
        # Arrange
        category_page = CategoryPage(browser, self.link)
        # Act
        category_page.open()
        # Assert
        category_page.should_be_main_page_link()

    def test_go_to_main_page(self, browser):
        # Arrange
        category_page = CategoryPage(browser, self.link)
        category_page.open()
        # Act
        category_page.go_to_main_page()
        main_page = MainPage(browser, browser.current_url)
        # Assert
        main_page.should_be_welcome_text()

    def test_go_to_next_page(self, browser):
        # Arrange
        category_page = CategoryPage(browser, self.link)
        category_page.open()
        # Act
        category_page.scroll_page_down()
        category_page.go_to_next_page()
        # Assert
        category_page.should_be_previous_page_link()
