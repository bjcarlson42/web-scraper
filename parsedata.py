from bs4 import BeautifulSoup
import requests
import json

# urlToScrape = "https://benjamincarlson.net/"
# response = requests.get(urlToScrape, timeout=5)
# content = BeautifulSoup(response.content, "html.parser")

# workExperienceObject = {
#     "name": content.find('h4', attrs={'class': 'experience-h4'}),
#     "employer": content.find('h5', attrs={'class': 'experience-h5'}),
#     "date": content.find('p', attrs={'class': 'experience-p'})
# } 

# work_experience_dict = json.loads(workExperienceObject)

# work_json = json.dumps(work_experience_dict)



# 1. python JSOn to dict
# person = '{"name": "Ben", "languages": ["English", "Spanish"]}'
# person_dict = json.loads(person)
# print(person_dict)

# 2. python to read JSON file
# with open('data.json') as f:
#     data = json.load(f)
# print(data)

# 3. Convert dict to JSON
# person_ditc = {'name': 'Bob', 'age': '12', 'children': 'none'}
# person_json = json.dumps(person_ditc)
# print(person_json)

# 4. Writing JSON to a file
# person_dict = {"name": "Bob",
#                "languages": ["English", "Fench"],
#                "married": True,
#                "age": 32
#                }
# with open('person.txt', 'w') as json_file:
#     json.dump(person_dict, json_file)
