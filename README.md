# Sentiment-Analysis-With-String-Matching
Analisis sentimen berita ekonomi atau finansial dengan menggunakan algoritma pencocokan string
## :scroll: Deskripsi
Penerapan algoritma pencocokan string dilakukan pada setiap judul dari sebuah berita ekonomi. Pola yang digunakan adalah kata kunci yang dianggap merepresentasikan suatu sentimen terhadap ekonomi. Metode pengambilan judul berita akan menggunakan bantuan dari News API dan Web Scrapping. Proses analisis akan dimulai dengan pengambilan data menggunakan News API dan Scrapping situs – situs berita. Pencarian dengan News API akan difokuskan untuk memperoleh judul berita dengan topik ekonomi dengan memanfaatkan parameter kategori yang sudah tersedia dalam News API. Data yang sudah diambil akan diproses terlebih dahulu sehingga analisis dan data dapat Selanjutnya akan dilakukan penentuan kata kunci dan pencocokan string oleh beberapa algoritma pencocokan string, kali ini metode pencocokan string yang digunakan adalah brute force, KnuthMorris-Pratt, dan Boyer Moore

## :warning: Requirement
Lakukan instalasi terhadap beberapa library berikut dengan meng-copy kode ke dalam terminal atau command prompt
- Python
- Python Library \
BeautifulSoup
`pip install beautifulsoup4` \
Request
`pip install request` \
Ntlk
`pip install nltk` \

## :writing_hand: Authors
Henry Anand Septian Radityo
