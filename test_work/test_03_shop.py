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

   driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
   driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
   driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

   driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
   
   driver.find_element(By.CSS_SELECTOR, "#checkout").click()

   driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Bob")
   driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Bobs")
   driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("12346", Keys.RETURN)

   total_sum = driver.find_element(
        By.CSS_SELECTOR, "div.summary_total_label").text

   print(total_sum)

   driver.quit()

   assert total_sum == "Total: $58.29"




   


