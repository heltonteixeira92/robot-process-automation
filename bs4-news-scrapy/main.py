"""
Webscraping using bs4 and requests.
There are limitations if need to scroll the page to get more content,
in this case selenium could be better.
"""

import requests
import bs4
from datetime import date

url = 'https://g1.globo.com/tecnologia/'

response = requests.get(url)

page = bs4.BeautifulSoup(response.text, "html.parser")

news_list = page.find_all("a", class_="feed-post-link")

today = date.today()


# append news title and link
file = open("news.txt", "a")
file.write(today.strftime("\n%d-%m-%Y\n"))

for news in news_list:
    file.write(f"\n{news.text}")
    file.write(f"\n{news.get('href')}\n")

file.close()
