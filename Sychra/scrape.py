import requests
import os
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def download_images(url, output_folder='book_images'):
    output_folder = "C:\Users\ondra\dokumenty\WebScrape"
    response = requests.get(url)

    if response.status_code == 200:
    
        os.makedirs(output_folder, exist_ok=True)
        output_folder = 'C:\Users\ondra\dokumenty\WebScrape'
        soup = BeautifulSoup(response.text, 'html.parser')
        
        image_tags = soup.find_all('img')
        for index, img_tag in enumerate(image_tags):
            image_url = urljoin(url, img_tag['src'])
            image_response = requests.get(image_url)

            if image_response.status_code == 200:
                # Save the image to the output folder
                with open(os.path.join(output_folder, f"image_{index + 1}.jpg"), 'wb') as img_file:
                    img_file.write(image_response.content)
                print(f"Image {index + 1} downloaded successfully.")
            else:
                print(f"Failed to download image {index + 1}. Status code:", image_response.status_code)

    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)

# Replace 'https://books.toscrape.com/' with the URL of the website you want to scrape
download_images('https://books.toscrape.com/')