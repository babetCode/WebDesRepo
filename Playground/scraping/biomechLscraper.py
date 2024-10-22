import requests
from bs4 import BeautifulSoup

# Step 1: Define the base URL of the forum page
base_url = "https://biomch-l.isbweb.org/forum/biomch-l-forums/jobs-and-positions"

# Step 2: Send a GET request to the webpage with headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def get_topics_from_page(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 4: Find all topic titles with both classes ('topic-title' and 'js-topic-title')
    topics = soup.find_all('a', class_=['topic-title', 'js-topic-title'])

    # Step 5: Filter and print topics that contain the word "internship" (case insensitive)
    for topic in topics:
        title = topic.get_text().strip()
        if 'internship' in title.lower():  # Case insensitive search for 'internship'
            # Ensure the link is a full URL
            topic_url = topic['href']
            if not topic_url.startswith('http'):
                topic_url = f"https://biomch-l.isbweb.org/{topic_url}"  # Handle relative URLs
            print(f"\033[97mTopic: {title}\033[0m")
            print(f"\033[94mLink: {topic_url}\n\033[0m")

# Step 6: Implement pagination by looping through pages
page_number = 3
while True:
    # Construct the URL for each page (assumes pagination uses '?page=N')
    page_url = f"{base_url}/page{page_number}"
    print(f"\033[90mScraping page {page_number}: {page_url}\033[0m")
    
    get_topics_from_page(page_url)
    
    # Check if there is a next page (look for pagination controls)
    response = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Find the "Next" link to know if there are more pages (adjust selector based on page)
    next_button = soup.find('a', class_='js-pagenav-next-button')  # Adjust based on actual class/structure
    if next_button:
        page_number += 1  # Move to the next page
    else:
        break  # No more pages, exit loop
