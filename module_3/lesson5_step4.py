from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_id("input_value").text
    browser.execute_script("window.scrollBy(0, 150);")
    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)

finally:
    time.sleep(10)
    browser.quit()
