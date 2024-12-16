from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Firefox_driver = webdriver.Firefox()

Firefox_driver.get("http://the-internet.herokuapp.com/login")

username_f = Firefox_driver.find_element(By.XPATH, "//input[@type='text']")
username_f.send_keys("tomsmith")
password_f = Firefox_driver.find_element(By.XPATH, "//input[@type='password']")
password_f.send_keys("SuperSecretPassword!")


login_buttonf = Firefox_driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_buttonf.click()

Firefox_driver.quit()