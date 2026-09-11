from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://txelectricce.com") # The TX Electric website

input("Login and start the course, then press ENTER...") # His password is random, save it here when you reset his password.

while True:
    try:
        timer = driver.find_element(By.CLASS_NAME, "countdown").text.strip()
        print("Timer:", timer)

        if timer == "":
            print("Timer finished -> submitting form")

            next_button = driver.find_element(By.NAME, "btnNext")
            next_button.click()

            time.sleep(5)

        else:
            time.sleep(2)

    except Exception as e:
        print("Waiting...", e)
        time.sleep(2)
