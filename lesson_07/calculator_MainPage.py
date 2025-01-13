from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        
        self.delay_input = (By.ID, "delay")
        self.seven_button = (By.XPATH, "//span[text() = '7']")
        self.plus_button = (By.XPATH, "//span[text() = '+']")
        self.eight_button = (By.XPATH, "//span[text() = '8']")
        self.equals_button = (By.XPATH, "//span[text() = '=']")
        self.result_display = (By.CLASS_NAME, "screen")

    def open(self):
        self.browser.get(self.url)

    def enter_delay(self, delay):
        delay_input = self.browser.find_element(self.delay_input)
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_calculator_buttons(self):
        self.browser.find_element(self.seven_button).click()
        self.browser.find_element(self.plus_button).click()
        self.browser.find_element(self.eight_button).click()
        self.browser.find_element(self.equals_button).click()

    def get_result(self):
        WebDriverWait(self.browser, 46).until(
            EC.text_to_be_present_in_element(self.result_display, "15")
        )
        return self.browser.find_element(self.result_display).text