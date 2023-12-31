import requests
import os
import time
import string
from nltk import word_tokenize

ROOT_PATH = os.getcwd()
SCRAPE_PATH = 'C:/Users/NTB/Downloads'



for i in range(1,51):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    page = requests.get(url)
    text = page.text
    
    #print(url)

    web_lines = text.splitlines() 

    images_url = []

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
        
    for i in images_url_et_names:
        #print(i, images_url_et_names[i])
        img_url = images_url_et_names[i][0]
        img_name = images_url_et_names[i][1]
    
        downloadurl = f"https://books.toscrape.com/catalogue/" +  img_url
        response = requests.get(downloadurl)

        for t in string.punctuation:
             while t in img_name:
                  img_name = img_name.replace(t,"")
    
        with open(os.path.join(SCRAPE_PATH, f'{img_name}.jpg'), 'wb') as out_file:
                out_file.write(response.content)
                print('\t', downloadurl, img_name, 'downloaded')
            
        time.sleep(1)

