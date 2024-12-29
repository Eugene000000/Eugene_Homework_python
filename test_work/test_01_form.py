from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

def test1():
   driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

   first_name = driver.find_element(By.CSS_SELECTOR, '[name="first-name"]')
   first_name.send_keys("Иван")

   last_name = driver.find_element(By.CSS_SELECTOR, '[name="last-name"]')
   last_name.send_keys("Петров")

   Address = driver.find_element(By.CSS_SELECTOR, '[name="address"]')
   Address.send_keys("Ленина, 55-3")

   zip_code = driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]')
   zip_code.send_keys("")

   city = driver.find_element(By.CSS_SELECTOR, '[name="city"]')
   city.send_keys("Москва")

   country = driver.find_element(By.CSS_SELECTOR, '[name="country"]')
   country.send_keys("Россия")

   email = driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]')
   email.send_keys("test@skypro.com")

   phone = driver.find_element(By.CSS_SELECTOR, '[name="phone"]')
   phone.send_keys("+7985899998787")

   job = driver.find_element(By.CSS_SELECTOR, '[name="job-position"]')
   job.send_keys("QA")

   company = driver.find_element(By.CSS_SELECTOR, '[name="company"]')
   company.send_keys("SkyPro")

   driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

   driver.find_element(By.CSS_SELECTOR, '[class="alert py-2 alert-danger"]')
   red_color = '#f8d7da'
   color_zip = zip_code.get_property(By.CSS_SELECTOR, '[class="alert py-2 alert-danger"]')
   assert color_zip == red_color

   green_color = '#d1e7dd'
   fields = [first_name, last_name, Address, zip_code, city, country, email, phone, job, company]
   for field in fields:
     color_fields = field.get_property(By.CSS_SELECTOR, '[class="alert py-2 alert-success"]')
   assert green_color == color_fields

   driver.quit()