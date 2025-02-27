from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MainPage:
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

    def open(self):
        self.driver.get(self.url)

    def fill_form(self, first_name, last_name, address, email, phone, zip_code, city, country, job_position, company):
        self.driver.find_element(*self._first_name).send_keys(first_name)
        self.driver.find_element(*self._last_name).send_keys(last_name)
        self.driver.find_element(*self._address).send_keys(address)
        self.driver.find_element(*self._email).send_keys(email)
        self.driver.find_element(*self._phone).send_keys(phone)
        self.driver.find_element(*self._zip_code).send_keys(zip_code)
        self.driver.find_element(*self._city).send_keys(city)
        self.driver.find_element(*self._country).send_keys(country)
        self.driver.find_element(*self._job_position).send_keys(job_position)
        self.driver.find_element(*self._company).send_keys(company)

    def submit(self):
        self.driver.find_element(*self._submit_button).click()

    def get_zip_code_field_color(self):
        self._zip_code = (By.ID, "zip-code")
        return self.driver.find_element(*self._zip_code).value_of_css_property('border-color')  # Проверка цвета поля

    def get_other_fields_color(self):
        self._first_name = (By.ID, "first-name")
        self._last_name = (By.ID, "last-name")
        self._address = (By.ID, "address")
        self._email = (By.ID, "e-mail")
        self._phone = (By.ID, "phone")
        self._city = (By.ID, "city")
        self._country = (By.ID, "country")
        self._job_position = (By.ID, "job-position")
        self._company = (By.ID, "company")
        
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