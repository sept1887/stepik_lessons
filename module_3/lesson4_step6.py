from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    x = browser.find_element_by_id("input_value").text
    browser.execute_script("window.scrollBy(0, 150);")
    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(calc(x))
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector("button.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()