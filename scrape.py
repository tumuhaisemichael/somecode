import requests
from bs4 import BeautifulSoup
import json

# URL of the website to scrape
url = 'https://www.ugandacoffee.go.ug/'

# Send a GET request to the website
response = requests.get(url)
# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract all text
all_text = soup.get_text()

# Extract all links
links = soup.find_all('a')
all_links = [link.get('href') for link in links]

# Extract all images
images = soup.find_all('img')
all_images = [img.get('src') for img in images]

# Extract all tables
tables = soup.find_all('table')
all_tables = [str(table) for table in tables]

# Save data to a JSON file
data = {
    "text": all_text,
    "links": all_links,
    "images": all_images,
    "tables": all_tables
}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
