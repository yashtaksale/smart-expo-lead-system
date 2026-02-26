import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def send_whatsapp_message(phone, name):

    def run():
        try:
            message = f"""Dear {name},
Greetings from Microtronics.
Thank you for visiting our stall and sharing your valuable time with us.
Hope we will have a meeting very soon.
Please confirm your convenient schedule to meet.
Microtronics Team."""

            service = Service("chromedriver.exe")

            options = webdriver.ChromeOptions()

            options.add_argument(
                r"--user-data-dir=C:\Users\yasht\AppData\Local\Google\Chrome\User Data"
            )
            options.add_argument("--profile-directory=Default")

            driver = webdriver.Chrome(service=service, options=options)

            driver.get(f"https://web.whatsapp.com/send?phone={phone}")

            wait = WebDriverWait(driver, 40)

            box = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, '//div[@contenteditable="true"]')
                )
            )

            box.click()
            box.send_keys(message)
            box.send_keys(Keys.ENTER)

            time.sleep(5)
            driver.quit()

        except Exception as e:
            print("WhatsApp Error:", e)

    threading.Thread(target=run).start()