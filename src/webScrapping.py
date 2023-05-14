import requests
from bs4 import BeautifulSoup

url = "https://www.kompas.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

judul_h1 = soup.find_all("h1")
judul_h2 = soup.find_all("h2")

list_judul = []
for judul in judul_h1:
    list_judul.append(judul.text)

for judul in judul_h2:
    list_judul.append(judul.text)

for el in list_judul:
    print(el)
