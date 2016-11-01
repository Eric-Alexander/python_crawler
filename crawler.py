
#ADVENTURES IN CRAWLING: finding total count of links/how many times each link is present

from urllib2 import urlopen

from bs4 import BeautifulSoup

import pprint
# plug in any url HERE:
url = 'http://www.metalsucks.net'

#can use "xml", "lxml" or "html.parser"
soupy = BeautifulSoup(urlopen(url), "html.parser")

#print (soupy.prettify())
list_of_urls = []
for link in soupy.find_all('a'):
    list_of_urls.append(link.get('href'))
urls_dict = {}

#create a dictionary where key = link and value = number of link found while parsing
for urls in list_of_urls:
    if not urls in urls_dict:
        urls_dict[urls] = 1
    else:
        urls_dict[urls] += 1
print urls_dict
