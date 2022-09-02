from pytest import fixture
from selenium import webdriver

@fixture(scope='session')#function
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser

    #Teardown
    print("teaering down the browser")