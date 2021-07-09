# importation des modules
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-web-security')
options.add_argument('--disable-xss-auditor')
BASE_URL = 'https://www.bing.com/search?q={}&form=QBLH&sp=-1&pq={}&sc=1-26&qs=n&sk=&cvid=3DFB266916C24C8AB266E798C9171AC9'
PATH = 'drivers\chromedriver.exe'
def generatorBingLinks(word_search):
    word_search = word_search.replace(' ','+')
    url = BASE_URL.format(word_search,word_search)
    return url
driver= webdriver.Chrome(PATH,options=options)
def getArticles(link):
    articles = []
    driver.get(link)
    link_xpath = driver.find_elements_by_tag_name('cite')
    for i in range(len(link_xpath)):
        article = link_xpath[i].text
        articles.append(article)
    print(articles)

getArticles(generatorBingLinks('Apprendre a faire du scraping avec python'))


