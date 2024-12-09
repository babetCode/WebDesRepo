import requests
from bs4 import BeautifulSoup

# Step 1: Define the URL of the forum page
url = "https://biomch-l.isbweb.org/forum/biomch-l-forums/jobs-and-positions"

# Step 2: Send a GET request to the webpage
response = requests.get(url)

# Step 3: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Find all topic titles (you need to inspect the webpage to find the correct tag)
# On inspecting the forum page, topic titles are usually within <a> tags
topics = soup.find_all('a', class_='topic-title')

# Step 5: Filter and print topics that contain the word "internship"
for topic in topics:
    title = topic.get_text()
    if 'internship' in title.lower():  # Case insensitive search for 'internship'
        topic_url = topic['href']
        print(f"Topic: {title}")
        print(f"Link: {topic_url}\n")
