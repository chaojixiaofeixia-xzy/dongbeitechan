from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """所有页面类的基类，封装通用操作"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, locator):
        """等待元素出现并返回"""
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def find_clickable(self, by, locator):
        """等待元素可点击并返回"""
        return self.wait.until(EC.element_to_be_clickable((by, locator)))

    def click(self, by, locator):
        """点击元素"""
        element = self.find_clickable(by, locator)
        element.click()

    def type(self, by, locator, text):
        """输入文本"""
        element = self.find_element(by, locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, locator):
        """获取元素文本"""
        return self.find_element(by, locator).text

    def get_title(self):
        """获取页面标题"""
        return self.driver.title