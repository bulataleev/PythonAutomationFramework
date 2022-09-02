from email.policy import default
from pytest import fixture
from selenium import webdriver

@fixture(scope='session')#function
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser

    #Teardown
    print("teaering down the browser")

def pytest_addoption(parser):
    parser.addoption("--env", action="store", help="env to run tests")