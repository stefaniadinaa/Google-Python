import bs4
import requests
from bs4 import BeautifulSoup

URL = "https://lpf.ro/liga-1"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")#first_liga = results.find_all("div", class_="card-content")
#parsed_html = bs4.BeautifulSoup.find_all(class = "container main-content content-pagina-clasament")
match = soup.find('table', class_ = "clasament_general white-shadow")

print(match)