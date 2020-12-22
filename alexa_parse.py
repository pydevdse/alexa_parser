import requests,  json
from lxml import html
from pprint import pprint

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

class Alexa:
    def __init__(self,domen):
        self.page = requests.get('https://www.alexa.com/siteinfo/'+domen,headers=headers)
        self.tree = html.fromstring(self.page.content)
    
    def recursion_print_list(self, obj_list):
        #print('--------------------------------- recursion --------------------------------')
        for o in obj_list:
            if isinstance(o, list):
                #print('------list------')
                self.recursion_print_list(o)
                continue
            if isinstance(o, dict):
                #print('--json--')
                for key, value in o.items():
                    print(key, value)
                continue
            print('not list and not json:', o)

    @property
    def visitorPercentage(self):
        j = self.tree.xpath('//*[@id="visitorPercentage"]/text()')
        vp = json.loads(j[0])
        for v in vp:
            for key, value in v.items():
                print(key, value)

    def topKeywords(self):
        j = self.tree.xpath('//*[@id="topKeywordsJSON"]/text()')
        vp = json.loads(j[0])
        for key, value in vp.items():
            if isinstance(value, list):
                print('-----------key----------', key)
                self.recursion_print_list(value)

    def rankDataWindow(self):
        j = self.tree.xpath('//*[@id="rankDataWindow"]/text()')
        vp = json.loads(j[0])
        pprint(vp)
    
    @property
    def rankData(self):
        j = self.tree.xpath('//*[@id="rankData"]/text()')
        vp = json.loads(j[0])
        pprint(vp)

if __name__ == '__main__':
    google = Alexa('google.com')
    google.rankData
    mail_ru = Alexa('mail.ru')
    mail_ru.visitorPercentage
    alexa = Alexa('alexa.com')
    alexa.topKeywords()

