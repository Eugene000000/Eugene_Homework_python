from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MainPage:

    def __init__(self, driver): 
        self.driver = driver
        self.url = ("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        self.first_name = (By.CSS_SELECTOR, '[name="first-name"]')
        self.last_name = (By.CSS_SELECTOR, '[name="last-name"]')
        self.address = (By.CSS_SELECTOR, '[name="address"]')
        self.zip = (By.CSS_SELECTOR, '[name="zip-code"]')
        self.city = (By.CSS_SELECTOR, '[name="city"]')
        self.country = (By.CSS_SELECTOR, '[name="country"]')
        self.email = (By.CSS_SELECTOR, '[name="e-mail"]')
        self.phone = (By.CSS_SELECTOR, '[name="phone"]')
        self.job = (By.CSS_SELECTOR, '[name="job-position"]')
        self.company = (By.CSS_SELECTOR, '[name="company"]')
        self.submit_button = (By.CSS_SELECTOR, '[type="submit"]')

    def open(self):
        self.driver.get(self.url)  

    def data_for_form(self, first_name, last_name, address, zip, city, country, email, phone, job, company):
        self.driver.find_element(self.first_name).send_keys(first_name)
        self.driver.find_element(self.last_name).send_keys(last_name)
        self.driver.find_element(self.address).send_keys(address)
        self.driver.find_element(self.email).send_keys(email)
        self.driver.find_element(self.phone).send_keys(phone)
        self.driver.find_element(self.zip).send_keys(zip)
        self.driver.find_element(self.city).send_keys(city)
        self.driver.find_element(self.country).send_keys(country)
        self.driver.find_element(self.job_position).send_keys(job)
        self.driver.find_element(self.company).send_keys(company)     

    def submit(self):
        self.driver.find_element(self.submit_button).click()

    def get_zip_code_field_color(self):
        self._zip_code = (By.ID, "zip-code")
        return self.driver.find_element(self.zip).value_of_css_property('border-color') 

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
            'first_name': self.browser.find_element(self.first_name).value_of_css_property('border-color'),
            'last_name': self.browser.find_element(self.last_name).value_of_css_property('border-color'),
            'address': self.browser.find_element(self.address).value_of_css_property('border-color'),
            'email': self.browser.find_element(self.email).value_of_css_property('border-color'),
            'phone': self.browser.find_element(self.phone).value_of_css_property('border-color'),
            'city': self.browser.find_element(self.city).value_of_css_property('border-color'),
            'country': self.browser.find_element(self.country).value_of_css_property('border-color'),
            'job_position': self.browser.find_element(self.job_position).value_of_css_property('border-color'),
            'company': self.browser.find_element(self.company).value_of_css_property('border-color'),
        }      
           
