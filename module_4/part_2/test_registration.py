from selenium import webdriver
from selenium.webdriver.common.by import By

def test_registration():
    # Data
    main_page_link = "http://selenium1py.pythonanywhere.com/"
    user_name_value = "secrets-inside@yandex.ru"
    password_value = "Ussur692527"
    exp_success_msg = "Спасибо за регистрацию!"

    login_link_locator = "login_link"
    user_name_locator = "id_registration-email"
    password_locator = "id_registration-password1"
    password_repeat_locator = "id_registration-password2"
    submit_btn_locator = "registration_submit"
    success_msg_locator = "alertinner.wicon"

    try:
        #Arrange
        browser = webdriver.Chrome()
        browser.get(main_page_link)
        login_link = browser.find_element(By.ID, login_link_locator)
        login_link.click()

        #Act
        user_name = browser.find_element(By.ID, user_name_locator)
        user_name.send_keys(user_name_value)
        password = browser.find_element(By.ID, password_locator)
        password.send_keys(password_value)
        password_repeat = browser.find_element(By.ID, password_repeat_locator)
        password_repeat.send_keys(password_value)
        submit_btn = browser.find_element(By.NAME, submit_btn_locator)
        submit_btn.click()

        #Assert
        success_msg = browser.find_element(By.CLASS_NAME, success_msg_locator)
        success_msg = success_msg.text
        assert success_msg == exp_success_msg, \
            f'Expected message is "{exp_success_msg}", but actual message is "{success_msg}"'

    finally:
        browser.quit()