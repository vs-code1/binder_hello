import requests
from bs4 import BeautifulSoup

res = requests.get('https://testbook.com/question-answer/sitemap/question-bank.xml')

soup = BeautifulSoup(res.content, 'lxml')
loc= soup.find_all('loc')
with open('textbook_questions1.txt', 'w', encoding='utf-8') as file:
    for item in loc:
        file.write(item.text)
        file.write('\n')