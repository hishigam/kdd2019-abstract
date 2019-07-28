import json
import sys

if len(sys.argv) < 2:
    print('usage: python3 keyword_search.py ')
    sys.exit(-1)

with open('kdd2019_abstract.json', 'rt') as f:
    titles = json.load(f)

extracted_titles = list()
for title in titles.keys():
    abstract = titles[title].get('abstract', '')
    for keyword in sys.argv[1:]:
        if keyword in abstract or keyword.capitalize() in abstract:
            print(title)
            extracted_titles.append(title)
            break

print(len(extracted_titles))
