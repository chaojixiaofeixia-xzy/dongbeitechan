import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    """每个测试用例提供独立的浏览器实例"""
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()