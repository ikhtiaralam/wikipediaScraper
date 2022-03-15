# Import packages
import requests
from bs4 import BeautifulSoup

class Scraper():

    def scrapdata(self):

        subject = 'Heidenheim an der Brenz'

        url = 'https://en.wikipedia.org/w/api.php'
        params = {
            'action': 'parse',
            'page': subject,
            'format': 'json',
            'prop':'text',
            'redirects':''
        }
        response = requests.get(url, params=params)
        data = response.json()
        
        raw_html = data['parse']['text']['*']
        soup = BeautifulSoup(raw_html,'html.parser')
        soup.find_all('p')
        text = ''
        
        for p in soup.find_all('p'):
            text += p.text
        
        print(text[:100000])
        print('Text length: ', len(text))
        wikilist = []
        
        wikilist.append(text[:100000])
        wikilist.append(len(text))

        return wikilist
             
wiki = Scraper()

wiki.scrapdata()

# Abstract example ##########################################################

# import requests
 
# subject = 'React (JavaScript library)'
# url = 'https://en.wikipedia.org/w/api.php'
# params = {
#         'action': 'query',
#         'format': 'json',
#         'titles': subject,
#         'prop': 'extracts',
#         'exintro': True,
#         'explaintext': True,
#     }
 
# response = requests.get(url, params=params)
# data = response.json()
 
# page = next(iter(data['query']['pages'].values()))
# print(page['extract'][:50])




# Make a search of a topic with srsearch ####################################

# import requests
 
# query = 'javascript'
 
# url = 'https://en.wikipedia.org/w/api.php'
# params = {
#             'action':'query',
#             'format':'json',
#             'list':'search',
#             'utf8':1,
#             'srsearch':query
#         }
 
# data = requests.get(url, params=params).json()
 
# for i in data['query']['search']:
#     print(i['title'], ' - Word count: ', i['wordcount'])