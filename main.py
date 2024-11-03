import requests
from bs4 import BeautifulSoup
import json

base_url = f"https://quotes.toscrape.com"
data = []


def get_quotes(url):
    response = requests.get(base_url, timeout=10)
    bs = BeautifulSoup(response.text, features="html.parser")
    quote = bs.find_all(class_="quote")
    for q in quote:
        text = q.find(class_='text').text
        author = q.find(class_='author').text
        tags = [tag.get_text() for tag in q.find_all(class_='tag') ]
        print(text)
        print(author)
        print(tags)
        data.append({'quote': text, 'author': author, 'tags': tags})


# Достаем данные постраннично
page = 1
while True:
    url = f"{base_url}page/{page}/"
    res = requests.get(url)
    if "No quotes found!" in res.text:
        break
    get_quotes(url)
    page += 1


# Сохранение данных в JSON-файл
with open("quotes.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
