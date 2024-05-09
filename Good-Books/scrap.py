from bs4 import BeautifulSoup
import requests

# URL of the page you want to scrape, 'fiction' or 'non-fiction'
url = "https://www.goodbooks.io/top-100/fiction"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the elements containing the book titles and authors
# This will depend on the actual HTML structure of the page
lists = soup.find('div', class_="grid-books grod-books-top-100 w-dyn-items")
titles = lists.find_all('h5')
authors = lists.find_all('h6')

# Extract and print the titles and authors
for index, (title, author) in enumerate(zip(titles, authors), start=1):
    print(f"{index}|{title.text.strip()}|{author.text.strip()}")
