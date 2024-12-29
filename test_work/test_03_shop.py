from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

driver.get("https://www.saucedemo.com/")

login = driver.find_element(By.CSS_SELECTOR, "#user-name")
login.send_keys("standard_user")

password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("secret_sauce", Keys.RETURN)

sleep(5)

product1 = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-lads-backpack").click()

product2 = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sause-labs-bolt-t-shirt").click()

product3 = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sause-labs-onesie").click()

cart = driver.find_element(By.CSS_SELECTOR, "#shopping_cart_link").click()

checkout = driver.find_element(By.CSS_SELECTOR, "#checkout").click()

first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
first_name.send_keys("Bob")

last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
last_name.send_keys("Bobs")

zip = driver.find_element(By.CSS_SELECTOR, "#postal-code")
zip.send_keys("12346", Keys.RETURN)

txt = driver.find_element(By.CSS_SELECTOR, "summery_total_label").text
print(txt)

finish = driver.find_element(By.CSS_SELECTOR, "#finish").click()

driver.quit()





   


