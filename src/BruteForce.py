import NewsAPI as news

# kata untuk sentiment positif dan negatif
positive_words = ['beda', 'tampang', 'begini', 'buyback', 'saham', 'sukses', 'mudah', 'menarik', 'penuh', 'baik', 'puas', 'mantap', 'kolaborasi', 'dividen', 'cuan', 'prospektif', 'menggiurkan', 'pameran', 'laba', 'meluncur', 'profit', 'cemerlang', 'nyaman', 'terkerek', 'berumur', 'bagus', 'bangga']
negative_words = ['penipuan', 'rusak', 'mengecewakan', 'ribet', 'mahal', 'berisiko', 'seram', 'terbatas', 'buruk', 'sakit', 'menyebalkan', 'berseteru', 'rusuh', 'batal', 'tersandera', 'intervensi', 'pemalsuan', 'bangkrut', 'kerugian', 'bumerang', 'tak layak']

titles = news.getTitle()
clean_titles = []
for title in titles:
    clean_title = title.rsplit("-", 1)[0].strip()
    clean_titles.append(clean_title)
def driverBF(titles):
    for title in titles:
        title = title.lower()
        title = title.replace(",", "").replace(".", "")
        words = title.split()

        sentiment_score = 0
        for word in words:
            print(word, end=' ')
            for positive_word in positive_words:
                if len(positive_word)<len(word):
                    for i in range (len(word)):
                        if (word[i:i+len(positive_word)] == positive_word):
                            sentiment_score += 1

            for negative_word in negative_words:
                if len(negative_word)<len(word):
                    for i in range (len(word)):
                        if (word[i:i+len(negative_word)] == negative_word):
                            sentiment_score -= 1
        print()
        if sentiment_score > 0:
            sentiment = "Positive"
        elif sentiment_score < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        print("Title:", title)
        print("Sentiment:", sentiment)
        print()


driverBF(clean_titles)