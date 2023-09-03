import urllib.request

#
from bs4 import BeautifulSoup

class RetriveLinks:

    def __init__(self, webSite):
        self.webSite = webSite

    def ShowLinks(self, showChild = False):
        site = urllib.request.urlopen(self.webSite)
        
        bea = BeautifulSoup(site, "html.parser")

        links = bea('a')

        print('\r\n Links main page \r\n')

        for l in links: 
            #print(l)           
            print(l.contents[0], '>>', l.get('href'))
            #print('Content:', l.contents)            
            #print('Attributes:', l.attrs)
            #print('\n'
            
        if showChild :            
            print('\r\n Links child page \r\n')

            for l in links: 
                link = l.get('href', None)

                print('Search links:', link)

                try:
                    if link[0:4] == 'http':
                        content = urllib.request.urlopen(link)
                    else:
                        content = urllib.request.urlopen(self.webSite + link)

                    bea2 = BeautifulSoup(content, 'html.parser')

                    new_links = bea2('a')

                    if len(new_links) > 0:
                        for l in links: 
                            print(l.get('href'))
                    else:
                        print('No links')
                except:
                    print('No links!')

    