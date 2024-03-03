import requests
import json
import time

URL="https://app.rakuten.co.jp/services/api/BooksTotal/Search/20170404"

payload = {
  'format':'json',
  'applicationId':'1042938514760951306',
  'booksGenreId':'000',
  'keyword':'Python',
  'page':1
}

books = []
while True:
    response = requests.get(URL, params=payload)
    data = json.loads(response.text)
    books.extend(data["Items"])
    if data["pageCount"] == data["page"]:
      break
    payload["page"] = data["page"] + 1
    time.sleep(1)
  
with open("rakuten_books.json", "w") as f:
  json.dump(books, f)