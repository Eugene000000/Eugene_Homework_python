import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:

    """Класс с методами для работы на сайте калькулятора"""

    def __init__(self, browser):
        self.browser = browser
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self._delay_input = (By.ID, "delay")
        self._seven_button = (By.XPATH, "//span[text() = '7']")
        self._plus_button = (By.XPATH, "//span[text() = '+']")
        self._eight_button = (By.XPATH, "//span[text() = '8']")
        self._equals_button = (By.XPATH, "//span[text() = '=']")
        self._result_display = (By.CLASS_NAME, "screen")

    @allure.step("Открыть сайт с калькулятором")
    def open(self):
        self.browser.get(self.url)

    @allure.step("Заполнить поле ожидания")
    def enter_delay(self, delay: str) -> None:

        """
        Функция служит для отчистки поля и введения необходимого времени ожидания
        """

        with allure.step("Отчистить поле"):
            delay_input = self.browser.find_element(*self._delay_input)
            delay_input.clear()
        with allure.step("Ввод времени ожидания"):
            delay_input.send_keys(delay)

    @allure.step("Выполнение операции")
    def click_calculator_buttons(self) -> None:
        """
        Функция служит для проведения вычислительной операции.
        Порядок действий:
        1. Нажать кнопка с цифрой '7'
        2. Нажать кнопка с знаком '+'
        3. Нажать кнопка с цифрой '8'
        4. Нажать кнопка с знаком '='
        """
        with allure.step("Нажать кнопку с цифрой '7'"):
            self.browser.find_element(*self._seven_button).click()
        with allure.step("Нажать кнопку с цифрой '+'"):
            self.browser.find_element(*self._plus_button).click()
        with allure.step("Нажать кнопку с цифрой '8'"):
            self.browser.find_element(*self._eight_button).click()
        with allure.step("Нажать кнопку с цифрой '='"):
            self.browser.find_element(*self._equals_button).click()
        
    @allure.step("Проверить, что в результате вычислений отображена цифра '15'")
    def get_result(self):

        """
        Функция служит для проверки результата вычислений суммы чисел 7 и 8
        """
        WebDriverWait(self.browser, 46).until(
        EC.text_to_be_present_in_element(self._result_display, "15")
        )
        return self.browser.find_element(*self._result_display).text
