# import_data_to_es.py

import json
from elasticsearch7 import Elasticsearch

with open('rakuten_books.json','r') as f:
    rakuten_books=json.load(f)

es = Elasticsearch(hosts="http://localhost:9200")

for rakuten_book in rakuten_books:
    rakuten_book_item=rakuten_book['Item']
    try:
        es.create(index='book',id=rakuten_book_item['isbn'],body=rakuten_book_item)
    except:
        pass
    print('{}created'.format(rakuten_book_item['title']))

