import urllib3
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json
from writing_xml import write_xml

proxy_servers = {
   'http': 'http://proxy.sample.com:8080',
   'https': 'http://secureproxy.sample.com:8080',
}

# Extracting all important data
class ExtractText(BeautifulSoup):
    def __init__(self, html):
        self.html = html

    def all_html(self):
        self.soup = BeautifulSoup(self.html, 'html.parser')

    def get_catagory(self):
        bread = ''
        self.catagory = self.soup.find_all('span', {'class': 'item'})
        if self.catagory == None:
            bread = "NO-BREAD-CRUMB-FOUND"
        else:
            for item in self.catagory:
                bread += item.text
                bread += ','

        return bread
    def get_question(self):
        self.question = self.soup.find('h1', {'class': 'questionBody tag-h1'})
        if self.question == None:
            return 'NO QUESTION FOUND'
        else:
            return self.question

    def get_question_exam(self):
        self.question_date = self.soup.find('div', {'class': 'pure-u-1 pure-u-md-11-24 pure-u-lg-10-24 pure-u-xl-10-24'})
        if (self.question_date == None):
            return 'NO EXAM DATE PROVIDED.'
        else:
            return self.question_date

    def get_options(self):
        self.options = self.soup.find_all('div', {'class': 'options'})
        if self.options == None:
            return "No options found."
        else:
            return self.options
    
    def get_answer(self):
        self.answer = self.soup.find('div', {'class': 'card answer-card'}).find('div')
        if self.answer == None:
            return 'no answer found.'
        else:
            return self.answer.text

    def get_solution(self):
        self.solution = self.soup.find('div', {'class': 'solution'})
        self.solution.find('div', {'class': 'buttons-container'}).decompose()
        if self.solution == None:
            return "no solution found"
        else:
            return self.solution

    
# return all questoin urls
def get_urls():
    with open('urls_textbook.txt') as file:
        data = file.read()
        urls = data.split('\n')

    return urls

# sending request to site
def send_request(url):
    ua = UserAgent()
    header = ua.random
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    print(response.status)

urls = get_urls()
x = 10
y = 0
url = ''
send_request(urls[2])
# for url in urls:
#     pass
#     print(url)

    # obj_1 = ExtractText(html)
    # obj_1.all_html()
    # cata = obj_1.get_catagory()
    # que = obj_1.get_question()
    # que_e = obj_1.get_question_exam()
    # opt = obj_1.get_options()
    # ans = obj_1.get_answer()
    # sol = obj_1.get_solution()
    # write_xml(url, cata, que, que_e, opt, ans, sol)