import allure
import pytest
from selenium import webdriver
from shop_MainPage import ShopPage

@pytest.fixture
def chrome_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.id("lesson_10")
@allure.story("Покупка товаров в магазине")
@allure.feature("SHOPPING")
@allure.epic("Интернет-магазин")
@allure.title("Проверка соответствия итоговой суммы с выбранными товарами")
@allure.description("Проверка итоговой суммы в интернет-магазине вычисляется корректно при выборе товара")
@allure.severity("blocker")
def test_shopping(chrome_browser):
    shopping_page = ShopPage(chrome_browser)
    shopping_page.open()
    shopping_page.login("standard_user", "secret_sauce")
    shopping_page.add_to_cart()
    shopping_page.checkout("Имя", "Фамилия", "12345")

    total = shopping_page.get_total()
    assert total == "Total: $58.29"