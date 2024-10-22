user_name = "z41z517"
pass_word = 'wRiteItdown1?'
search = 'adrien'

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

print("Waiting for Duo 2FA approval... Please approve the login on your mobile device.")

WebDriverWait(driver, 30).until(
    EC.url_contains("https://api-160ed6ec.duosecurity.com/frame/v4/auth/prompt")
)
print("Navigated to Duo 2FA page.")

duo_push_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "dont-trust-browser-button"))  # Adjust CSS selector as needed
)
duo_push_button.click()

print("2FA approved, continuing...")

# page_content = driver.page_source
# Print or save the page content as needed
# print(page_content)

for i in range(30):
    print(30-i, end=' ', flush=True)
    time.sleep(1)
# Close the driver when done
driver.quit()

# https://www.montana.edu/cope/emp-dir/api/directory-v2.php?query=ab&queryType=students