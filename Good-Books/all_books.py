from bs4 import BeautifulSoup
import requests

base_url = "https://www.goodbooks.io/books"

# Initialize a counter for the current page
page_number = 1
book_number = 1
# Loop through the pages
while True:
    # Construct the URL for the current page
    url = f"{base_url}?216112dc_page={page_number}"
    # Send a GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the elements containing the book titles and authors
        lists = soup.find('div', class_="grid-books")
        titles = lists.find_all('h5', class_="grid-item-title")
        authors = lists.find_all('h6', class_="grid-item-subtitle")
        
        # Extract and print the titles and authors
        for title, author in zip(titles, authors):
            print(f"{book_number}|{title.text.strip()}|{author.text.strip()}")
            book_number += 1
        
        # Increment the page number
        page_number += 1
        
        # Break the loop if we've reached the last page
        if page_number > 253:
            break
    else:
        print(f"Failed to retrieve page {page_number}.")
        break

