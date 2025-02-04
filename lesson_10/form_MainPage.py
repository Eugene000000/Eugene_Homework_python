import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MainPage:
    """Класс с методами для тестирования формы"""

    def __init__(self, driver):
         self.driver = driver
         self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

         self._first_name = (By.NAME, "first-name")
         self._last_name = (By.NAME, "last-name")
         self._address = (By.NAME, "address")
         self._email = (By.NAME, "e-mail")
         self._phone = (By.NAME, "phone")
         self._zip_code = (By.NAME, "zip-code")
         self._city = (By.NAME, "city")
         self._country = (By.NAME, "country")
         self._job_position = (By.NAME, "job-position")
         self._company = (By.NAME, "company")
         self._submit_button = (By.TAG_NAME, "button")

    @allure.step("Открыть страницу с формой")
    def open(self):
          self.driver.get(self.url)
    @allure.step("Заполнить форму")
    def fill_form(self, first_name: str, last_name: str, address: str, email: str, phone: str, zip_code: str, city: str, country: str, job_position: str, company: str) -> None:
       with allure.step("Заполнить поле 'First name'"):
            self.driver.find_element(*self._first_name).send_keys(first_name)
            """
            Функция находит поле "First name" и заполняет его 
            """

       with allure.step("Заполнить поле 'Last name'"):
            self.driver.find_element(*self._last_name).send_keys(last_name)
            """
            Функция находит поле "Last name" и заполняет его 
            """
       with allure.step("Заполнить поле 'Address'"):
            self.driver.find_element(*self._address).send_keys(address)
            """
            Функция находит поле "address" и заполняет его 
            """
       with allure.step("Заполнить поле 'Email'"):
            self.driver.find_element(*self._email).send_keys(email)
            """
            Функция находит поле "email" и заполняет его 
            """
       with allure.step("Заполнить поле 'Phone'"):
            self.driver.find_element(*self._phone).send_keys(phone)
            """
            Функция находит поле "phone" и заполняет его 
            """
       with allure.step("Не заполнить поле 'Zip_code'"):
            self.driver.find_element(*self._zip_code).send_keys(zip_code)
            """
            Функция находит поле "zip_code" и не заполняет его 
            """
       with allure.step("Заполнить поле 'City'"):
            self.driver.find_element(*self._city).send_keys(city)
            """
            Функция находит поле "city" и не заполняет его 
            """
       with allure.step("Заполнить поле 'Country'"):
            self.driver.find_element(*self._country).send_keys(country)
            """
            Функция находит поле "country" и не заполняет его 
            """
       with allure.step("Заполнить поле 'Job'"):
            self.driver.find_element(*self._job_position).send_keys(job_position)
            """
            Функция находит поле "job_position" и не заполняет его 
            """
       with allure.step("Заполнить поле 'Company'"):
            self.driver.find_element(*self._company).send_keys(company)
            """
            Функция находит поле "company" и не заполняет его 
            """
        
    @allure.step("Нажатие на кнопку SUBMIT")
    def submit(self) -> None:
        self.driver.find_element(*self._submit_button).click()
        """
        Эта функция для нажимания кнопки "Submit"
        """
    @allure.step("Проверка цвета поля ZIP_CODE, оно красное")
    def get_zip_code_field_color(self) -> None:
        self._zip_code = (By.ID, "zip-code")
        return self.driver.find_element(*self._zip_code).value_of_css_property('border-color')  # Проверка цвета поля
    
    @allure.step("Проверка цветов других полей, они зелёные")
    def get_other_fields_color(self) -> None:
        self._first_name = (By.ID, "first-name")
        self._last_name = (By.ID, "last-name")
        self._address = (By.ID, "address")
        self._email = (By.ID, "e-mail")
        self._phone = (By.ID, "phone")
        self._city = (By.ID, "city")
        self._country = (By.ID, "country")
        self._job_position = (By.ID, "job-position")
        self._company = (By.ID, "company")
        """
        Функция для проверки цветов заполненных полей, а именно в зеленый цвет:
        """
        return {
            'first_name': self.driver.find_element(*self._first_name).value_of_css_property('border-color'),
            'last_name': self.driver.find_element(*self._last_name).value_of_css_property('border-color'),
            'address': self.driver.find_element(*self._address).value_of_css_property('border-color'),
            'email': self.driver.find_element(*self._email).value_of_css_property('border-color'),
            'phone': self.driver.find_element(*self._phone).value_of_css_property('border-color'),
            'city': self.driver.find_element(*self._city).value_of_css_property('border-color'),
            'country': self.driver.find_element(*self._country).value_of_css_property('border-color'),
            'job_position': self.driver.find_element(*self._job_position).value_of_css_property('border-color'),
            'company': self.driver.find_element(*self._company).value_of_css_property('border-color'),
            }
            