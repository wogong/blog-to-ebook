from calibre.web.feeds.recipes import BasicNewsRecipe
 
class Catcoding(BasicNewsRecipe):
    
    title = '程序员的喵'
    description = '技术、写作、英语、个人成长相关主题'
    cover_url = ''
 
    url_prefix = 'https://catcoding.me/'
    no_stylesheets = True
    #keep_only_tags = [{ 'class': 'chapter' }]

 
    def parse_index(self):
        soup = self.index_to_soup(self.url_prefix + '/archives/')
 
        archives = soup.find('div', { 'class': 'archives-container' })
        feeds = []
 
        for section in archives.findAll('section'):
            articles = []
            section_name = section.find('h1').text.strip()
            posts = section.findAll('div', {'class': 'section-list-item'})
            for post in posts:
                date = post.find('p', {'class': 'archive-date'}).text
                title = date + post.find('a', {'class': 'archive-title'}).text
                link = self.url_prefix + post.find('a', {'class': 'archive-title'})['href']
                articles.append({'title': title, 'url': link})
            feeds.append((section_name, reversed(articles)))

        return feeds