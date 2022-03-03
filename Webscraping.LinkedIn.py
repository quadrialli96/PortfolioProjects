import requests
from bs4 import BeautifulSoup as bs


linkedin_user = input('Input LinkedIn User: ')
url = 'https://linkedin.com/' + linkedin_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', {'alt': 'Quadri Alli'})['src']
print(profile_image)
