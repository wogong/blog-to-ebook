from calibre.web.feeds.recipes import BasicNewsRecipe
 
class Geohot(BasicNewsRecipe):
 
    title = 'the singularity is nearer'
    url_prefix = 'https://geohot.github.io'
    no_stylesheets = True
    keep_only_tags = [dict(name='main', attrs={'class': 'page-content'})]

    def parse_index(self):
        soup = self.index_to_soup(self.url_prefix + '/blog')
 
        div = soup.find('ul', { 'class': 'post-list' })
 
        articles = []
        for link in div.findAll('li'):
            date =  link.find('span', {'class': 'post-meta'}).text.strip()
            title = date + ' ' + link.find('a', {'class': 'post-link'}).text.strip()
            url = self.url_prefix + link.find('a', {'class': 'post-link'})['href'] 
            articles.append({ 'title': title, 'url': url })
 
        ans = [('Geohot', reversed(articles))]
 
        return ans