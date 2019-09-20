'''
inflection
requests
beautifulsoup / pip install beautifulsoup4
'''

import requests
from bs4 import BeautifulSoup
from inflection import titleize

def title_generator(links):
	titles = []

	def post_formatter(url):
		if 'posts' in url:
			url = url.split('/')[-1]
			url = url.replace('-',' ')
			url = titleize(url)
			titles.append(url)

	for link in links:
		post_formatter(link['href'])


	return titles

r = requests.get('https://www.dailysmarty.com/topics/python')
r.text

soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('a')

titles = title_generator(links)

for title in titles:
	print(title)