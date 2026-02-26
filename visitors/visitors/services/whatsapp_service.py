from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:8000/entry-mode/") 
print("Page Title:", driver.title)


driver.get("http://127.0.0.1:8000/signup/")


driver.find_element(By.NAME, "name").send_keys("John Doe")
driver.find_element(By.NAME, "phone").send_keys("1234567890")
driver.find_element(By.NAME, "company").send_keys("Tech Corp")
driver.find_element(By.NAME, "email").send_keys("john@example.com")
driver.find_element(By.NAME, "message").send_keys("Hello, I am a test visitor.")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)
if "thanks" in driver.current_url:
    print("Signup Successful! Redirected to Thanks page.")

driver.get("http://127.0.0.1:8000/export-visitors-excel/")
print("Export request sent.")

time.sleep(5)
driver.quit()