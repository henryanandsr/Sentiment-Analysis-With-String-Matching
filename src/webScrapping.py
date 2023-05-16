import requests
from bs4 import BeautifulSoup

url = "https://www.kompas.com/"
url2 = "https://www.detik.com/"
url3 = "https://www.tribunnews.com/"
url4 = "https://www.liputan6.com/"
url5 = "https://www.cnbcindonesia.com/"
url6 = "https://www.cnnindonesia.com/"
url7 = "https://www.beritasatu.com/"
url8 = "https://www.beritagar.id/"
url9 = "https://www.beritajakarta.id/"
url10 = "https://www.beritajatim.com/"
url11 = "https://www.beritabali.com/"
url12 = "https://www.beritajogja.id/"
url13 = "https://www.beritamalukuonline.com/"
url14 = "https://www.beritapapua.id/"
url15 = "https://www.beritapapua.co/"
url16 = "https://www.beritapapuabarat.com/"
url17 = "https://www.beritapapuabarat.co/"
url18 = "https://www.beritapapuabarat.id/"
url19 = "https://www.beritapapuabarat.net/"
url20 = "https://www.beritapapuabarat.org/"

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
