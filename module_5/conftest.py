import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='Choose language: ru, en-GB, es or fr')


@pytest.fixture(scope='function')
def browser(language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope='session')
def language(request):
    return request.config.getoption('language')
