import pytest
from selenium import webdriver
from calculator_MainPage import CalculatorPage

@pytest.fixture
def chrome_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator_form(chrome_browser):
    calc_page = CalculatorPage(chrome_browser)
    calc_page.open()

    calc_page.enter_delay(45)

    calc_page.click_calculator_buttons()

    result_text = calc_page.get_result()

    assert result_text == "15", f"Expected result to be '15', but got '{result_text}'"