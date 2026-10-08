from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
wait=WebDriverWait(driver,10)
driver.get("https://vinothqaacademy.com/demo-site/")
driver.maximize_window()


first_name=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//input[@id="vfb-5"]')
    )
)
first_name.send_keys("Hareesh")

print("Attribute +xpath using  id attribue executed")
last_name=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//input[@name="vfb-7"]')
    )
)

last_name.send_keys("Rajendran")
print("Attribute +xpath  using name attribute executed")

gender=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[text()="Male"]')
    )
)
if not gender.is_selected():
    gender.click()

print("xpath using text() attribute")
print("radiobox attribute used")

course=wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH,'//*[starts-with(@type,"checkbox")]')
    )
)
for cour in course:
    if not cour.is_selected():
        driver.execute_script(
            "arguments[0].click();",
            cour
        )
    else:
        driver.execute_script(
                    "arguments[0].click();",
                    cour
                )


print("starts-with xpath used")
print("checbox attribute used")

street=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[@type="text" and @id="vfb-13-address"]')
    )
)
street.send_keys("Saveetha nagar")
print("And xpath are used")

bulding=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//input[@name="vfb-13[address-2]" or @id="vfb-13-address-2"]')
    )
)
bulding.send_keys("Saveetha Engineering College")

print("OR xpath are used")

city=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//input[contains(@name,"vfb-13[city]")]')
    )
)
city.send_keys("Chennai")

print("Contains() xpath are used")

state=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[@name="vfb-13[state]"]')
    )
)

state.send_keys("TamilNadu")

pincode=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[@id="vfb-13-zip"]')
    )
)

pincode.send_keys("602105")

country=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[@id="vfb-13-country"]')
    )
)

dropdown=Select(country)
dropdown.select_by_value("India")



print("dropdown select using xpath executed")

email=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[@id="vfb-14"]')
    )
)
email.send_keys("hareeshraja2006@gmail.com")

conv_time=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[@id="vfb-18"]')
    )
)
conv_time.send_keys("10/08/2026")

hours=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[@id="vfb-16-hour"]')
    )
)

dropdown_02=Select(hours)

dropdown_02.select_by_index(1)

mins=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[@name="vfb-16[min]"]')
    )
)

dropdown_03=Select(mins)

dropdown_03.select_by_index(3)

print("dropdown by index success")

mobile=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[@name="vfb-19"]')
    )
)

mobile.send_keys("1234567890")

query=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[@name="vfb-23"]')
    )
)
query.send_keys("Nil")

captcha=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[@id="vfb-3"]')
    )
)

captcha.send_keys("33")

print(captcha.tag_name)

print("Parent xpath success")

submit=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[@id="vfb-4"]')
    )
)

driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    submit
)

driver.execute_script(
        "arguments[0].click();",
    submit
)


print("Form Submitted Successfully  ")

time.sleep(30)
