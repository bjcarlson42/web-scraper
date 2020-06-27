from bs4 import BeautifulSoup
import requests, json, re

urlToScrape = "http://www.cnbc.com"
response = requests.get(urlToScrape, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

def get_top_news_headline(obj):
    a_tags = obj.find('div', {'id':'MainContent'}).find_all('a', {'href':re.compile('.*cnbc.*')})
    print('Latest News Headline***********')
    print(a_tags[0].get_text())

def get_latest_news_headline(obj):
    pass   

get_top_news_headline(content)
get_latest_news_headline(content)
