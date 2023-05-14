import requests

def getTitle():
    api_key = 'de3b0228aaac4cc69bfbdce911c16985'
    url = f'https://newsapi.org/v2/top-headlines?country=id&category=business&apiKey={api_key}'
    num_pages = 5

    titles = []
    for page in range(1, num_pages + 1):
        page_url = f'{url}&page={page}'
        response = requests.get(page_url)

        if response.status_code == 200:
            data = response.json()
            articles = data['articles']

            for article in articles:
                title = article['title']
                titles.append(title)
        else:
            print('Error occurred:', response.status_code)

    return titles
