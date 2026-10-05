from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
username=driver.find_element(By.ID,"user-name")
username.send_keys("standard_user")
password=driver.find_element(By.ID,"password")
password.send_keys("secret_sauce")
login=driver.find_element(By.ID,"login-button")
login.click()

products=driver.find_elements(By.CLASS_NAME,"inventory_item_name ")

for item in products:
    print(item.text)
time.sleep(10)
