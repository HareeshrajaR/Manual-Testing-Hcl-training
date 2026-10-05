from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")

wait = WebDriverWait(driver, 10)

login = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, '//a[.//span[text()="Login"]]')
    )
)
driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    login
)

driver.execute_script(
        "arguments[0].click();",
    login
)

enter=wait.until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME,"jwCbxy")
    )
)

enter.send_keys("9361331044")

continue_button=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[@id="container"]/div/div[1]/div[2]/div[2]/div/div/div[3]/div/button')
    )
)
continue_button.click()

verify=wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[@id="container"]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/button')
    )
)

driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    verify
)
driver.execute_script(
    "arguments[0].click();",
    verify
)

time.sleep(30)

