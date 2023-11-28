from google.oauth2 import service_account
from googleapiclient.discovery import build
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


# set up credentials
creds = service_account.Credentials.from_service_account_file(
    './google_sheets_api_keys.py',
    scopes=[os.getenv('SCOPES')])

# set up API client
service = build('sheets', 'v4', credentials=creds)

# specify the sheet and range you want to retrieve data from
sheet_id = os.getenv('SHEET_ID')
sheet_range = os.getenv('SHEET_RANGE')

# retrieve data from the sheet
result = service.spreadsheets().values().get(spreadsheetId=sheet_id, range=sheet_range).execute()
rows = result.get('values', [])

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

# print the data
for row in rows:
    print("URL string: ", str(row))
    driver.get(str(row[4]))
    time.sleep(5)

    edit_button = driver.find_element(By.XPATH, os.getenv('EDIT_BUTTON_PATH2'))
    edit_button.click()
    time.sleep(5)

    listing_name = driver.find_element(By.XPATH, os.getenv('LISTING_NAME3'))
    listing_name.click()
    driver.execute_script("arguments[0].value = '';", listing_name)
    listing_name.send_keys(Keys.DELETE)
    print(str(row[5]))
    listing_name.send_keys(str(row[5]))

    listing_description = driver.find_element(By.XPATH, os.getenv('LISTING_DESCRIPTION1'))
    listing_description.click()    
    driver.execute_script("arguments[0].value = '';", listing_description)
    listing_description.send_keys(Keys.DELETE)
    listing_description.send_keys(str(row[6]))
    print("Checkpoint 1")

    listing_year = driver.find_element(By.XPATH, os.getenv('LISTING_YEAR'))
    listing_year.click()    
    driver.execute_script("arguments[0].value = '';", listing_year)
    listing_year.send_keys(Keys.DELETE)
    listing_year.send_keys(str(row[2]))
    print("Checkpoint 2")

    listing_plate = driver.find_element(By.XPATH, os.getenv('LISTING_PLATE'))
    listing_plate.click()    
    driver.execute_script("arguments[0].value = '';", listing_plate)
    listing_plate.send_keys(Keys.DELETE)
    listing_plate.send_keys(str(row[2]))
    print("Checkpoint 3")

    listing_seats = driver.find_element(By.XPATH, os.getenv('LISTING_SEATS'))
    listing_seats.click()    
    driver.execute_script("arguments[0].value = '';", listing_seats)
    listing_seats.send_keys(Keys.DELETE)
    listing_seats.send_keys(str(row[7]))
    print("Checkpoint 4")

    listing_doors = driver.find_element(By.XPATH, os.getenv('LISTING_DOORS'))
    listing_doors.click()    
    driver.execute_script("arguments[0].value = '';", listing_doors)
    listing_doors.send_keys(Keys.DELETE)
    listing_doors.send_keys(str(row[7]))
    print("Checkpoint 5")

    # Save the changes
    save_button = driver.find_element(By.XPATH, os.getenv('SAVE_BUTTON'))
    save_button.click()
    print("Boom, iteration done!")

driver.quit()