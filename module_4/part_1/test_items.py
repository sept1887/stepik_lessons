import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Data
main_page_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
btn_locator = 'button.btn-add-to-basket'
lang_locator = 'no-js'

exp_add_to_cart_btn_txt = {
    'ru': 'Добавить в корзину',
    'en-gb': 'Add to basket',
    'es': 'Añadir al carrito',
    'fr': 'Ajouter au panier'
}


def test_add_to_cart_btn_lang(browser, language):
    # Arrange
    browser.get(main_page_link)

    # Act
    add_to_cart_btn = browser.find_element(By.CSS_SELECTOR, btn_locator)
    page_lang = browser.find_element(By.CLASS_NAME, lang_locator).get_attribute('lang')
    language = language.lower() # Выглядит как костыль, но это пришлось сделать для бритиш инглиш --language=en-GB

    # Assert
    assert page_lang == language, \
        f'Expected page language is "{language}", but actual page language is "{page_lang}"'
    assert add_to_cart_btn.text in exp_add_to_cart_btn_txt[language], \
        f'Expected button text is "{exp_add_to_cart_btn_txt[language]}, but actual button text is "{add_to_cart_btn.text}"'