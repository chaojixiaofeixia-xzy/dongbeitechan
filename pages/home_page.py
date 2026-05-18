from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    """东北特产商城首页"""

    URL = "http://127.0.0.1:5000"

    # 页面元素定位器（集中管理，便于维护）
    PRODUCT_LIST = (By.CLASS_NAME, "product")
    PRODUCT_TITLE = (By.TAG_NAME, "h2")
    FIRST_ADD_BUTTON = (By.TAG_NAME, "button")
    CART_ITEMS = (By.ID, "cart-items")

    def open(self):
        """打开首页"""
        self.driver.get(self.URL)
        # 等待页面加载完成
        self.find_element(By.CLASS_NAME, "product")
        return self

    def get_page_title(self):
        """获取页面标题"""
        return self.get_title()

    def get_product_count(self):
        """获取商品数量"""
        products = self.driver.find_elements(*self.PRODUCT_LIST)
        return len(products)

    def get_first_product_name(self):
        """获取第一个商品的名称"""
        products = self.driver.find_elements(*self.PRODUCT_LIST)
        return products[0].find_element(*self.PRODUCT_TITLE).text

    def add_first_product_to_cart(self):
        """点击第一个商品的加入购物车按钮"""
        add_button = self.find_clickable(*self.FIRST_ADD_BUTTON)
        add_button.click()
        return self

    def get_cart_text(self):
        """获取购物车内容文本"""
        return self.get_text(*self.CART_ITEMS)