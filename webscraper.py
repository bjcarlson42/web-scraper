#Notes/all of my web scraping practice
#Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#Author: Benjamin Carlson
#Website: https://benjamincarlson.net/

from bs4 import BeautifulSoup
import requests

#variables
urlToScrape = "https://benjamincarlson.net/"
response = requests.get(urlToScrape, timeout=5)
#BeautifulSoup syntax
content = BeautifulSoup(response.content, "html.parser")

#returns the experience section
experience_section = content.find_all(id="experience")

#Prints all the text
content.prettify()

#extracting all URL's found on the page
for link in content.find_all('a'):
    print(link.get('href'))

#getting all the text
all_text = content.get_text()
print("Find all: ",content.find_all(["a", "br"]))

#using functions to find stuff
def has_class_but_no_id(content):
    return content.has_attr('class') and not content.has_attr('id')

print(content.find_all(has_class_but_no_id))

print(content.find_all('title'))

#searching by css class
print(content.find_all('p', class_="date"))

#searching by string
print(content.find_all(string="Benjamin"))
