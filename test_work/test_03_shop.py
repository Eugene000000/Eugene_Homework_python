from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shop(): 
   driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

   driver.get("https://www.saucedemo.com/")
   driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
   driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce", Keys.RETURN)

   driver.get("https://www.saucedemo.com/inventory.html")
   driver.find_element(By.ID, "#add-to-cart-sauce-lads-backpack").click()
   driver.find_element(By.ID, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
   driver.find_element(By.ID, "#add-to-cart-sauce-labs-onesie").click()

   driver.find_element(By.CSS_SELECTOR, "#shopping_cart_link").click()

   driver.get("https://www.saucedemo.com/cart.html")
   driver.find_element(By.CSS_SELECTOR, "#checkout").click()

   driver.get("https://www.saucedemo.com/checkout-step-one.html")
   driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Bob")
   driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Bobs")
   driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("12346", Keys.RETURN)

   driver.get("https://www.saucedemo.com/checkout-step-two.html")
   txt = driver.find_element(By.CSS_SELECTOR, "div.summery_total_label").text
   print(txt)

   driver.find_element(By.CSS_SELECTOR, "#finish").click()

   driver.quit()





   


