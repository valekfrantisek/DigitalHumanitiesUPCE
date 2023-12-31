# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import requests
import os
import time
from nltk import word_tokenize

ROOT_PATH = os.getcwd()
SCRAPE_PATH = 'C:/Users/kolle/Downloads'

url = "https://books.toscrape.com/"
page = requests.get(url)
text = page.text
print (text)

for i in range(1,51):
    url = f'https://books.toscrape.com/catalogue/page-{i}.html'
    page = requests.get(url)
    text = page.text
    print(url)


    web_lines = text.splitlines()
    images_url = []
    is_product = False
    for line in web_lines:
        if '<article class="product_pod">' in line:
        is_product = True
        if '<img src="' in line and is_product:
            start = line.find('<img src="')
            end = line.find('" alt="')
            img_url = line[start + 10:end]
            images_url.append(img_url)
            is_product = False

        print(images_url)
        print(len(images_url))

        for img_url in images_url:
        print(url + img_url)

        img_filename = img_url.split('/')[-1]

        response = requests.get(url + img_url)

        with open(os.path.join(SCRAPE_PATH, img_filename), 'wb') as out_file:
            out_file.write(response.content)
            print('\t', img_filename, 'downloaded')

        time.sleep(2)

        web_lines = text.splitlines()
        images_url_et_names = {}

        is_product = False

        for i, line in enumerate(web_lines):
            if '<article class="product_pod">' in line:
                is_product = True
            if '<img src="' in line and is_product:
                start = line.find('<img src="')
                end = line.find('" alt="')
                img_url = line[start + 10:end]

                start = line.find('" alt="')
                end = line.find('" class="thumbnail"')
                img_name = line[start + 7:end]

                images_url_et_names[i] = [img_url, img_name]
                is_product = False

        print('Urls and names retrieved.')

        for i in images_url_et_names:
            print(i, images_url_et_names[i])
            img_url = images_url_et_names[i][0]
            img_name = images_url_et_names[i][1]

            response = requests.get(url + img_url)

            with open(os.path.join(SCRAPE_PATH, f'{img_name}.jpg'), 'wb') as out_file:
                out_file.write(response.content)
                print('\t', img_name, 'downloaded')

            time.sleep(2)