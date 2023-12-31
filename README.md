# Description
This Python script is a basic web scraper designed to extract the title and all paragraph texts from a specified webpage. It uses the requests library to fetch the page content and BeautifulSoup from bs4 to parse and extract the required elements.

# Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`

# Installation
To set up this script, follow these steps:

1. Ensure Python 3.x is installed on your system.
2. Clone this repository or download the script file.
3. Install the required Python libraries.

# Usage
To run the script, use the following command in the terminal:

`python web_scraper.py`

The script is currently set to scrape `https://example.com`. Modify the `url` variable in the script to point to your desired webpage.

# Features
- Fetches the HTML content of a webpage using the requests library.
- Parses the HTML content and extracts the title and all paragraph texts using BeautifulSoup.
- Outputs the extracted data to the console.

# Configuration
No additional configuration is required. To scrape a different website, simply change the url variable in the script to the desired website's URL.

# Disclaimer
This script is for educational purposes only. Before scraping a website, ensure that you have permission and that your actions comply with the website's terms of service or use policy. Some websites explicitly forbid web scraping in their terms of service.
