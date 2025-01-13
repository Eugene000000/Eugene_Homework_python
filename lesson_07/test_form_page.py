import pytest
from selenium import webdriver
from form_MainPage import MainPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  
    yield driver
    driver.quit()

def test_fill_form(chrome_browser):
    form_page = MainPage(chrome_browser)
    form_page.open()
    
    form_page.data_for_form(
        "Иван", 
        "Петров", 
        "Ленина, 55-3", 
        "test@skypro.com", 
        "+7985899998787", 
        "", 
        "Москва", 
        "Россия", 
        "QA", 
        "SkyPro"
    )
    form_page.submit()

    assert form_page.get_zip_code_field_color() == 'rgb(245, 194, 199)'
    colors = form_page.get_other_fields_color()
    for color in colors.values():
        assert color == 'rgb(186, 219, 204)'      





   