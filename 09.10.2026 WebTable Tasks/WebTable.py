from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.maximize_window()
driver.get("https://assertqa.com/practice/webtables")

employee_table=driver.find_element(By.ID,"employees-table")
header_tag=employee_table.find_elements(By.TAG_NAME,"th")
for head in header_tag:

    print(head.text,end=" ")
print("\nHeader Name was Printed Success")

rows=employee_table.find_elements(By.TAG_NAME,"tr")
first_row=rows[1]
first_row_data=first_row.find_elements(By.TAG_NAME,"td")
for data in first_row_data:
    print(data.text,end=" ")
print("\nFirst Row Data is printed")

last_rows=rows[-1]
last_rows_data=last_rows.find_elements(By.TAG_NAME,"td")
for data in last_rows_data:
    print(data.text,end=" ")
print("\nLast rows data printed Success")

last_name_search="smith"
for name in rows[1:]:
    row_data=name.find_elements(By.TAG_NAME,"td")
    if(row_data[2].text.strip().lower()==last_name_search.lower()):
        for data in row_data:
            print(data.text,end=" ")
        break
    else:
        print("employee Data Not Found")
print("\nEmployee Search Based on Last_Name")

for data in rows[1:]:
    row_data=data.find_elements(By.TAG_NAME,"td")
    print(row_data[3].text)
print("\nEmail of All rows Printed")

max_salary=0

for row in rows[1:]:
    row_data=row.find_elements(By.TAG_NAME,"td")
    salary=int(row_data[5].text.replace("$","").replace(",",""))
    max_salary=max(salary,max_salary)
print(max_salary)

print("\nMaximu Salary Printing Success")

links=employee_table.find_elements(By.TAG_NAME,"a")
if links:
    print("Links Exists")
    for link in links:
        print(link.text, link.get_attribute("href"))
else:
    print("FAIL - No links found in the table")
print("\nLink Checking Success")


count_data_rows=0
for data in rows[1:]:

    data_exists=data.find_elements(By.TAG_NAME,"td")
    if data_exists:
        count_data_rows+=1
print("Data Row Count: ",count_data_rows)
print("\nCount data rows without counting the header Success")



