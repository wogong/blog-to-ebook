'''failed, just using feed links'''

from calibre.web.feeds.recipes import BasicNewsRecipe
import json
import urllib.request

class laisky(BasicNewsRecipe):
 
    title = 'laisky-blog'
    url_prefix = 'https://blog.laisky.com/'
    no_stylesheets = True
    keep_only_tags = [dict(name='main', attrs={'class': 'page-content'})]

    def parse_index(self):
        url = 'https://gq.laisky.com/query/'
        headers = {
            'authority': 'gq.laisky.com',
            'accept': '/',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6,ja;q=0.5',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://blog.laisky.com',
            'referer': 'https://blog.laisky.com/',
            'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36'}

        data = {'query': 'query {\n            BlogPosts(\n                category_url: null,\n                page: {size: 200, page: 0},\n            ) {\n                title\n                name\n            }\n        }'}

        #response = requests.post(url, headers=headers, json=data)
        #data = response.json()
        req = urllib.request.Request(url, headers=headers, data=json.dumps(data).encode('utf-8'))
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
        blog_posts = data['data']['BlogPosts']
 
        articles = []
        for post in blog_posts:
            title = post['title']
            url = self.url_prefix + 'p/' + post['name'] + '/'
            articles.append({ 'title': title, 'url': url })
 
        ans = [('laisky', reversed(articles))]
 
        return ans