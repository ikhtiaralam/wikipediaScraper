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