import requests
from bs4 import BeautifulSoup

class Test():
    
    title = 'Test'
    description = ''
    cover_url = ''
 
    url_prefix = 'https://geohot.github.io'
    no_stylesheets = True
    keep_only_tags = [dict(class=['page-content'])]

    def index_to_soup(self, url):
        """
        This function process provided URL get its data using requets module
        and contrunct soup data using BeautifulSoup for scarping
        """
        requets_data = requests.get(url)
        if requets_data.status_code == 200:
            soup = BeautifulSoup(requets_data.text,'html')
            return soup

    def parse_index(self):
        soup = self.index_to_soup(self.url_prefix + '/blog')
 
        div = soup.find('ul', { 'class': 'post-list' })
 
        articles = []
        for link in div.findAll('li'): 
            title = link.find('a', {'class': 'post-link'}).text.strip()
            url = self.url_prefix + link.find('a', {'class': 'post-link'})['href'] 
            articles.append({ 'title': title, 'url': url })
 
        ans = [('Geohot', articles)]
 
        return ans

if __name__== '__main__':
    print ('Test')
    Test().parse_index()