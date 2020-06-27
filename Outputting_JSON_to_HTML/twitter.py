from bs4 import BeautifulSoup
import requests, json, re

urlToScrape = "https://twitter.com/DrueMarino"
response = requests.get(urlToScrape, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

name = content.find_all('span', {'class': re.compile('css-901oao')})
if(name == 0):
    print('null')
else:
    for n in name:
        print(n)


# drue_images = content.find_all('img', {'src': re.compile('.jpg')})
# for image in drue_images:
#     print(image['src']+'\n')
