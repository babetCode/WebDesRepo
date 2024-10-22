user_name = "z41z517"
pass_word = 'wRiteItdown1?'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Step 1: Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Step 2: Navigate to the login page
driver.get("https://www.montana.edu/search/students.html")

# Step 3: Wait for the login page to load and input your credentials
# Adjust the selectors as needed based on the page's HTML structure
username_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "username"))  # Change 'username' if incorrect ID
)
username_input.send_keys(user_name)

password_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "password"))  # Change 'password' if incorrect ID
)
password_input.send_keys(pass_word)

# Step 4: Submit the login form
login_button = driver.find_element(By.CSS_SELECTOR, ".btn-submit")  # Adjust based on the ID or button selector
login_button.click()

# Step 5: Handle Duo 2FA - Wait for iframe, switch to it
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))

# Wait for Duo prompt to appear (manually approve on your phone)
duo_push_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class*='push-button']"))  # Adjust CSS selector as needed
)
duo_push_button.click()

# Step 6: Wait for user to approve the 2FA on their mobile device
print("Waiting for Duo 2FA approval... Please approve the login on your mobile device.")

# Add a long wait to give time for you to approve the push
time.sleep(30)  # Adjust as needed, based on how long you need for the approval process

# Step 7: Once approved, Selenium will continue to the next page
print("2FA approved, continuing...")

# Step 8: Now, interact with the authenticated page or scrape the data
# Example: Extract content after successful login
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))  # Adjust based on page content
page_content = driver.page_source

# Print or save the page content as needed
print(page_content)

for i in range(30):
    print(30-i)
    time.sleep(1)
# Close the driver when done
driver.quit()
