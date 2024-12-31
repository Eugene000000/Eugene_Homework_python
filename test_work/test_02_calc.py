from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calc():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = driver.find_element(By.CSS_SELECTOR, '#delay')
    delay_input.clear()
    delay_input.send_keys("5")

    for value in ['7', '+', '8', '=']:
        driver.find_element(By.XPATH, f'//span[text()="{value}"]').click()

    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert int(result) == 15

    driver.quit()