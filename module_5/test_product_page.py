from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest


@pytest.mark.lesson5_step13
class TestUserAddToBasketFromProductPage:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    @pytest.fixture(scope="function", autouse=True)
    # Arrange
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user("secrets-inside@yandex.ru", "Ussur692527")
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # Act
        product_page = ProductPage(browser, self.link)
        product_page.open()
        # Assert
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        # Act
        product_page = ProductPage(browser, self.link)
        product_page.open()
        product_page.test_guest_can_add_product_to_basket()
        # Assert
        product_page.check_product_name_in_cart()
        product_page.check_price_in_cart()


class TestCasesForGuest:
    link_coders = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    link_city = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    link_reversing = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/reversing_202/"

    def test_guest_can_add_product_to_basket(self, browser):
        # Arrange
        product_page = ProductPage(browser, self.link_coders)
        product_page.open()
        # Act
        product_page.test_guest_can_add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        # Assert
        product_page.check_product_name_in_cart()
        product_page.check_price_in_cart()

    @pytest.mark.parametrize('promo_offer', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                                             pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        link = f"{self.link_coders}?promo={promo_offer}"
        # Arrange
        product_page = ProductPage(browser, link)
        product_page.open()
        # Act
        product_page.test_guest_can_add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        # Assert
        product_page.check_product_name_in_cart()
        product_page.check_price_in_cart()

    @pytest.mark.lesson5_step6
    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Arrange
        product_page = ProductPage(browser, self.link_coders)
        product_page.open()
        # Act
        product_page.add_to_cart_from_product_page()
        # Assert
        product_page.should_not_be_success_message()

    @pytest.mark.lesson5_step6
    def test_guest_cant_see_success_message(self, browser):
        # Arrange
        product_page = ProductPage(browser, self.link_coders)
        # Act
        product_page.open()
        # Assert
        product_page.should_not_be_success_message()

    @pytest.mark.lesson5_step6
    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Arrange
        product_page = ProductPage(browser, self.link_coders)
        product_page.open()
        # Act
        product_page.add_to_cart_from_product_page()
        # Assert
        product_page.success_msg_should_disappeared()

    @pytest.mark.lesson5_step8
    def test_guest_should_see_login_link_on_product_page(self, browser):
        # Arrange
        product_page = ProductPage(browser, self.link_city)
        # Act
        product_page.open()
        # Assert
        product_page.should_be_login_link()

    @pytest.mark.lesson5_step8
    def test_guest_can_go_to_login_product_page_from_product_page(self, browser):
        # Arrange
        product_page = ProductPage(browser, self.link_city)
        # Act
        product_page.open()
        # Assert
        product_page.should_be_login_link()

    @pytest.mark.lesson5_step10
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        product_page = ProductPage(browser, self.link_reversing)
        product_page.open()
        product_page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_items_in_basket()
        basket_page.should_be_empty_basket_msg()














