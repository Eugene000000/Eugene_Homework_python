from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
Firefox_driver = webdriver.Firefox()

Firefox_driver.get("http://the-internet.herokuapp.com/inputs")

input = Firefox_driver.find_element(By.XPATH, "//input[@type='number']")
input.send_keys("1000",Keys.RETURN)

input.clear()
input.send_keys("999",Keys.RETURN)

Firefox_driver.quit()