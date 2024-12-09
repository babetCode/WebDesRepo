"""
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

Code Status: In Progress
________________________________________________________________________

‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Author: | GitHub:| Email:  
_______________________________________________________________________________
"""

user_name = "z41z517"
pass_word = 'wRiteItdown1?'
download_path = 'C:/Users/goper/Downloads/stuscraped.csv'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import pandas as pd

# Step 1: Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Step 2: Navigate to page (this redirects to login)
driver.get("https://www.montana.edu/search/students.html")

# Step 3: Wait for the login page to load and input your credentials
username_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "username"))
)
username_input.send_keys(user_name)

password_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "password"))
)
password_input.send_keys(pass_word)

# Step 4: Submit the login form
login_button = driver.find_element(By.CSS_SELECTOR, ".btn-submit")
login_button.click()

print("Waiting for Duo 2FA approval... \
    Please approve the login on your mobile device.")

WebDriverWait(driver, 30).until(
    EC.url_contains(
        "https://api-160ed6ec.duosecurity.com/frame/v4/auth/prompt")
)
print("Navigated to Duo 2FA page.")

duo_push_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "dont-trust-browser-button"))
)
duo_push_button.click()

print("2FA approved, continuing...")

search_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "gsc-i-id1"))
)
search_input.send_keys('aa')

search_push_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".gsc-search-button"))
)
search_push_button.click()

time.sleep(1)

total_list = []

alphabet = [chr(i) for i in range(97, 123)]

for one in alphabet:
    for two in alphabet:
        driver.get(
            f"https://www.montana.edu/cope/emp-dir/api/directory-v2.php?\
            query={one}{two}&queryType=students"
        )
        body_text = driver.find_element(By.TAG_NAME, "body").text
        begining = body_text.find('[')
        end = body_text.rfind(']')
        useful_text = body_text[begining:end+1]
        useful_list = json.loads(useful_text)
        print(f'loading list from {one}{two}')
        counter = 0
        for item in useful_list:
            if item not in total_list:
                total_list.append(item)
                counter += 1
                print(counter, end=' ', flush=True)
print(len(total_list))
df = pd.DataFrame(total_list)
# df.to_csv(download_path)

for i in range(30):
    print(30-i, end=' ', flush=True)
    time.sleep(1)
# Close the driver when done
driver.quit()
