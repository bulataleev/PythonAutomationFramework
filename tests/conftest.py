from email.policy import default
from pytest import fixture
from selenium import webdriver
from config import Config

@fixture(scope='session')#function
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser

    #Teardown
    print("teaering down the browser")

def pytest_addoption(parser):
    parser.addoption("--env", action="store", help="env to run tests")

@fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


@fixture(scope="session")
def app_config(env):
    cfg = Config(env)
    return cfg