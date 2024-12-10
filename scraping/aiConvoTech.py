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
driver2 = webdriver.Chrome(service=service, options=chrome_options)

# Open the website
driver.get("https://copilot.microsoft.com/")
driver2.get("https://copilot.microsoft.com/")

# Print the title of the page
print(driver.title)
print(driver2.title)

# Click on the button with title "Get started"
sleep(2)
get_started_button = driver.find_element(By.CSS_SELECTOR, 'button[title="Get started"]')
get_started_button.click()
get_started_button2 = driver2.find_element(By.CSS_SELECTOR, 'button[title="Get started"]')
get_started_button2.click()

sleep(2)
user_input_box = driver.find_element(By.ID, "userInput")
user_input_box.send_keys("test")
user_input_box.send_keys(Keys.RETURN)
user_input_box2 = driver2.find_element(By.ID, "userInput")
user_input_box2.send_keys("test")
user_input_box2.send_keys(Keys.RETURN)

sleep(2)
next_button = driver.find_element(By.CSS_SELECTOR, 'button[title="Next"]')
next_button.click()
next_button2 = driver2.find_element(By.CSS_SELECTOR, 'button[title="Next"]')
next_button2.click()

sleep(2)
start_text = "Let's play a game: for the duration of this chat, you will act like a cs teacher who is teaching an introduction to burpsuite, I will be the student. you will maintain a neutral, casual tone, and never break character. you will be very blunt and not very encouraging. you will also make sure that we don't get off track and are always learning something new with each chat. I will start now: 'hello professor, what are we learning about in burpsuite today?"
user_input_box = driver.find_element(By.ID, "userInput")
# for char in start_text:
#         user_input_box.send_keys(char)
#         sleep(0.001)
user_input_box.send_keys(start_text)

start_text2 = "Let's play a game: for the duration of this chat, you will act like a cs student who is learning about burpsuite. at each chat, you will clarify you understanding of what I say and then ask a question about further functionality of burpsuite. We will start now:  "
user_input_box2 = driver2.find_element(By.ID, "userInput")
# for char in start_text2:
#         user_input_box2.send_keys(char)
#         sleep(0.001)
user_input_box2.send_keys(start_text2)

user_input_box.send_keys(Keys.RETURN)

sleep(5)
while True:
    last_div = driver.find_elements(By.CSS_SELECTOR, 'div.space-y-3.break-words')[-1]
    elements = last_div.find_elements(By.XPATH, ".//*")

    # Combine text from elements and remove line-return characters
    combined_text = " ".join(element.text.replace('\n', ' ') for element in elements)

    # Remove non-BMP characters
    combined_text = re.sub(r'[^\u0000-\uFFFF]', '', combined_text)

    # Split into sentences and remove duplicates while preserving order
    seen = set()
    unique_sentences = []
    for sentence in re.split(r'(?<=[.!?]) +', combined_text):
        if sentence not in seen:
            seen.add(sentence)
            unique_sentences.append(sentence)

    # Join the unique sentences back together
    combined_text = ' '.join(unique_sentences)

    # sleep(2)
    # user_input_box2 = driver2.find_element(By.ID, "userInput")
    # for char in combined_text:
    #     user_input_box2.send_keys(char)
    #     sleep(0.001)
    user_input_box2.send_keys(combined_text)

    # sleep(2)
    user_input_box2.send_keys(Keys.RETURN)

    sleep(10)

    last_div = driver2.find_elements(By.CSS_SELECTOR, 'div.space-y-3.break-words')[-1]
    elements = last_div.find_elements(By.XPATH, ".//*")

    combined_text = " ".join([element.text for element in elements])
    combined_text = re.sub(r'[^\u0000-\uFFFF]', '', combined_text)
    sentences = re.split(r'(?<=[.!?]) +', combined_text)

    # Use a set to remove duplicates while preserving order
    seen = set()
    unique_sentences = []
    for sentence in sentences:
        if sentence not in seen:
            seen.add(sentence)
            unique_sentences.append(sentence)

    # Join the unique sentences back together
    combined_text = ' '.join(unique_sentences)
    # print(combined_text)

    # sleep(2)
    user_input_box = driver.find_element(By.ID, "userInput")
    # for char in combined_text:
    #     user_input_box.send_keys(char)
    #     sleep(0.001)
    user_input_box.send_keys(combined_text + "also please remember to keep the lesson moving forward")

    # sleep(2)
    user_input_box.send_keys(Keys.RETURN)

    sleep(10)



# Wait for user input before closing the browsers
input("Press Enter to quit the browsers...")

# Close the browsers
driver.quit()
driver2.quit()