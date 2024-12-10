from time import sleep
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Set up Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode (commented out)

# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://voice.google.com/")

sleep(2)
sign_in_button = driver.find_element(By.CSS_SELECTOR, 'a[class="signUpLink"]')
sign_in_button.click()

sleep(2)
user_input_box = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')
user_input_box.send_keys("stickproduct2@gmail.com")
user_input_box.send_keys(Keys.RETURN)

# Wait for user input before closing the browsers

input("Press Enter to quit the browsers...")

# Close the browsers
driver.quit()
