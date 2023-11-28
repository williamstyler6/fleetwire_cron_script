from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Set up the webdriver
driver = webdriver.Chrome()

# Navigate to the Fleetwire.io login page
driver.get(os.getenv('LOGIN_URL'))

# Fill in the email and password fields and submit the form
email_field = driver.find_element("name", "email")
email_field.send_keys(os.getenv('DAYDREAM_EMAIL'))
password_field = driver.find_element("name", "password")
password_field.send_keys(os.getenv('DAYDREAM_PASS'))
password_field.submit()

# Wait for the login to complete and navigate to the listing page
WebDriverWait(driver, 7).until(EC.url_contains("fleetwire.io"))
driver.get(os.getenv('DRIVER'))
time.sleep(5)


# Click the "Edit" button next to "Vehicle Info"
edit_button = driver.find_element(By.XPATH, os.getenv('EDIT_BUTTON_PATH'))
edit_button.click()
time.sleep(5)

# Update the Listing Name input box
listing_name = driver.find_element(By.XPATH, os.getenv('LISTING_NAME2'))
listing_name.click()
driver.execute_script("arguments[0].value = '';", listing_name)
listing_name.send_keys(Keys.DELETE)
listing_name.send_keys("Susannnnn the Subaru!!!")

print("Made it to this testing point")
listing_name = driver.find_element(By.XPATH, os.getenv('LISTING_NAME1'))
listing_name.click()
driver.execute_script("arguments[0].value = '';", listing_name)
listing_name.send_keys(Keys.DELETE)
option_text = "Toyota"
option = driver.find_element(By.XPATH, os.getenv('OPTION_PATH'))
option.click()

# Save the changes
save_button = driver.find_element(By.XPATH, os.getenv('SAVE_BUTTON'))
save_button.click()

driver.quit()