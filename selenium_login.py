from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


options = webdriver.ChromeOptions()



driver = webdriver.Chrome(options=options)


driver.get("http://localhost:8000/login")


driver.find_element(By.NAME, "username").send_keys("akash")
driver.find_element(By.NAME, "password").send_keys("Akash.7788")
driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

time.sleep(2)

if "success" in driver.current_url.lower():
    print("Login successful!")
else:
    print("Login failed!")

driver.quit()
