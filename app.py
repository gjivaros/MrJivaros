# importation des modules
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# parametrage de chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-web-security')
options.add_argument('--disable-xss-auditor')
# url de base de recherche sur BING
BASE_URL = 'https://www.bing.com/search?q={}&form=QBLH&sp=-1&pq={}&sc=1-26&qs=n&sk=&cvid=3DFB266916C24C8AB266E798C9171AC9'

# path de chrome driver
PATH = 'drivers\chromedriver.exe'

# init driver
driver= webdriver.Chrome(PATH,options=options)


# fonction permettant de generer un lien de recherche BING
def generatorBingLinks(word_search):
    word_search = word_search.replace(' ','+')
    url = BASE_URL.format(word_search,word_search)
    print(url)
    return url

# fonction permettant de recuperer le liens des articles d'une recherche BING
def getArticles(link):
    articles = []
    driver.get(link)
    link_xpath = driver.find_elements_by_tag_name('cite')
    for i in range(len(link_xpath)):
        article = link_xpath[i].text
        articles.append(article)
    print(articles)
    return articles

getArticles(generatorBingLinks('Apprendre a faire du scraping avec python'))


