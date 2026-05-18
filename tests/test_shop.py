import allure
from pages.home_page import HomePage


@allure.feature("东北特产商城 - UI自动化测试")
class TestShopHomePage:

    @allure.story("页面标题验证")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_page_title(self, driver):
        home = HomePage(driver)
        home.open()
        assert "东北特产商城" in home.get_page_title()

    @allure.story("商品列表加载验证")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_product_list(self, driver):
        home = HomePage(driver)
        home.open()
        assert home.get_product_count() == 5
        assert home.get_first_product_name() == "五常大米"

    @allure.story("购物车功能验证")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_to_cart(self, driver):
        home = HomePage(driver)
        home.open()
        home.add_first_product_to_cart()
        assert "五常大米" in home.get_cart_text()