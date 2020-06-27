from bs4 import BeautifulSoup
import requests, json, re

urlToScrape = "https://twitter.com/DrueMarino"
response = requests.get(urlToScrape, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

drue_images = content.find_all('img', {'src': re.compile('.jpg')})
for image in drue_images:
    print(image['src']+'\n')

print('*********')

print(content.img.prettify())

# def get_top_news_headline(obj):
#     a_tags = obj.find('div', {'id': 'MainContent'}).find_all(
#         'a', {'href': re.compile('.*cnbc.*')})
#     print('Latest News Headline***********')
#     print(a_tags[0].get_text())
