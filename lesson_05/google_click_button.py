from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for i in range(5):
    and_button = driver.find_element(By.XPATH, ('//button[text()="addElement"]')).click()
    
    chrome_delete_buttons = driver.find_elements(By.XPATH, ('//button[text()="Delete"]'))
    
print(f"Список: {len(chrome_delete_buttons)}")

sleep(10)