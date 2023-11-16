#Tento kód jsem si musel upravit, původní kód mi nešel spustit ať jsem dělal co jsem dělal. S kódem mi pomohl brácha s kamarádem. Chatgpt mi vyhledal co mám importovat aby ten kód fungoval.

import re
import requests
import os
import time
from urllib.parse import urljoin

""" PATHS """
ROOT_PATH = os.getcwd()
SCRAPE_PATH = 'C:/Users/PetrPC/Downloads/Webscrape/'

""" Basic scrape settings. Retrieving web structure. """

for i in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"

    page = requests.get(url)
    text = page.text

    """ Downloading with image renamed. """

    web_lines = text.splitlines()

    images_url_et_names = {}

    is_product = False

    for j, line in enumerate(web_lines):
        if '<article class="product_pod">' in line:
            is_product = True
        if '<img src="' in line and is_product:
            start = line.find('<img src="')
            end = line.find('" alt="')
            img_url = line[start + 10:end]

            start = line.find('" alt="')
            end = line.find('" class="thumbnail"')
            img_name = line[start + 7:end]

            images_url_et_names[j] = [img_url, img_name]
            is_product = False

    print(f'Urls and names retrieved for page {i}.')

    for j in images_url_et_names:
        print(j, images_url_et_names[j])
        img_url = images_url_et_names[j][0]
        img_url_absolute = urljoin(url, img_url)
        img_name = re.sub(r'[^\w\s.-]', '', images_url_et_names[j][1])
        response = requests.get(img_url_absolute)

        with open(os.path.join(SCRAPE_PATH, f'{img_name}.jpg'), 'wb') as out_file:
            out_file.write(response.content)
            print('\t', img_name, 'downloaded')

            