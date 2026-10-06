from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://vinothqaacademy.com/demo-site/")
time.sleep(5)
First_name=driver.find_element(By.XPATH,'//*[@id="vfb-5"]')
First_name.send_keys("Hareesh")
Last_name=driver.find_element(By.NAME,"vfb-7")
Last_name.send_keys("R")
gender=driver.find_element(By.ID,"vfb-31-1")
if not gender.is_selected():
    gender.click()
    print("Gender Selected Success")
course_01=driver.find_element(By.ID,"vfb-20-0")
if not course_01.is_selected():
    course_01.click()
    print("Course_01 selected")
course_02=driver.find_element(By.ID,"vfb-20-1")
if not course_02.is_selected():
    course_02.click()
    print("Course_02 selected")
course_03=driver.find_element(By.ID,"vfb-20-3")
if  course_03.is_selected():
    course_03.click()
    print("Course_03 not  selected")
address=driver.find_element(By.ID,"vfb-13-address")
address.send_keys("Saveetha Engineering College,Chennai")
Street_address=driver.find_element(By.ID,"vfb-13-address-2")
Street_address.send_keys("SSE Building,Chennai")
state=driver.find_element(By.ID,"vfb-13-state")
state.send_keys("TamilNadu")
city=driver.find_element(By.ID,"vfb-13-city")
city.send_keys("Chennai")
postal_code=driver.find_element(By.ID,"vfb-13-zip")
postal_code.send_keys("602105")
Email=driver.find_element(By.ID,"vfb-14")
Email.send_keys("hareesh123@gmail.com")

time.sleep(20)
