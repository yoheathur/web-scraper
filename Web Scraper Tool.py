import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'https://example.com'
response = requests.get(url)
# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')
# Find and extract specific elements from the webpage
title = soup.title.text
paragraphs = soup.find_all('p')
# Print the extracted data
print('Title:', title)
print('Paragraphs:')
for p in paragraphs:
    print(p.text)