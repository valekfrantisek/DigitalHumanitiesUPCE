import requests
import os
import time
from nltk import word_tokenize
import string


ROOT_PATH = os.getcwd()
SCRAPE_PATH = 'C:/Users/Ukrainer/Downloads/'

def retreive_urls_et_names(url:str) -> dict:
    page = requests.get(url)
    text = page.text

    web_lines = text.splitlines()
    images_url_et_names = {}
    is_product = False

    for i, line in enumerate(web_lines):
        if '<article class="product_pod">' in line:
            is_product = True
        if '<img src="' in line and is_product:
            start = line.find('<img src="')
            end = line.find('" alt="')
            img_url = line[start+10:end]

            start = line.find('" alt="')
            end = line.find('" class="thumbnail"')
            img_name = line[start+7:end]

            images_url_et_names[i] = [img_url, img_name]
            is_product = False

    print('Urls and names retrieved.')
    return images_url_et_names


def download_image(img_data, img_name:str, path:str):
    with open(os.path.join(path, f'{img_name}.jpg'), 'wb') as out:
            out.write(img_data)
            print('\t', img_name, 'downloaded')
import string


for i in range(1,51):

    url = 'https://books.toscrape.com/catalogue/page-' + str(i) + '.html'
    images_url_et_names = retreive_urls_et_names(url)

    for i in images_url_et_names:
        img_url = images_url_et_names[i][0]
        img_name = images_url_et_names[i][1]
        while '&#39;' in img_name:
            img_name = img_name.replace('&#39;', "'")
        print(img_name)

        response = requests.get(url + img_url)
        img_data = response.content

        download_image(img_data, img_name, path=SCRAPE_PATH)
        time.sleep(1)
