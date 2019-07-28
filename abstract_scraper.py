import json
import urllib
from bs4 import BeautifulSoup

html = urllib.request.urlopen('https://www.kdd.org/kdd2019/proceedings')
soup = BeautifulSoup(html, "html.parser")

titles = dict(dict())
for link in soup.find_all('a'):
    if "DLtitleLink" in link.get('class', list()):
        titles[link.get_text()] = {'html': link.get('href')}

abstract_list = list()
for link in soup.find_all('div'):
    if "DLabstract" not in link.get('class', list()):
        continue
    abst_text = link.get_text()
    if len(abst_text) == 1:
        continue
    abstract_list.append(link.get_text())

assert len(titles) == len(abstract_list)

for title, abstract in zip(list(titles.keys()), abstract_list):
    titles[title].update({'abstract': abstract})

for title, abstract in zip(list(titles.keys()), abstract_list):
    titles[title].update({'abstract': abstract})

with open('kdd2019_abstract.json', 'w') as f:
    json.dump(titles, f, indent=2)

