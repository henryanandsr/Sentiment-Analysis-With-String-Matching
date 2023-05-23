import nltk
from nltk.corpus import opinion_lexicon

nltk.download('opinion_lexicon')

positive_words = set(opinion_lexicon.positive())
negative_words = set(opinion_lexicon.negative())

clean_titles = []
with open("transformed_text.txt", "r") as file:
    lines = file.readlines()
    clean_titles.extend(lines)

def preprocess_text(text):
    text = text.lower()
    text = text.replace(",", "").replace(".", "")
    return text

def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0 or n == 0 or m > n:
        return []

    last_occurrence = {}
    matches = []

    for i in range(m - 1, -1, -1):
        if pattern[i] not in last_occurrence:
            last_occurrence[pattern[i]] = i

    i = m - 1
    while i < n:
        j = m - 1
        k = i

        while j >= 0 and text[k] == pattern[j]:
            j -= 1
            k -= 1

        if j == -1:
            matches.append(k + 1)

        if text[i] in last_occurrence:
            i += m - min(j, 1 + last_occurrence[text[i]])
        else:
            i += m

    return matches

def driverBM(titles):
    title_list = []
    sentiment_list = []
    
    for title in titles:
        title = preprocess_text(title)
        words = title.split()

        sentiment_score = 0
        for word in words:
            if any(boyer_moore_search(word, positive_word) for positive_word in positive_words):
                sentiment_score += 1
            elif any(boyer_moore_search(word, negative_word) for negative_word in negative_words):
                sentiment_score -= 1

        if sentiment_score > 0:
            sentiment = "Positive"
        elif sentiment_score < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        print("Title:", title)
        print("Sentiment:", sentiment)
        print()
        title_list.append(title)
        sentiment_list.append(sentiment)



    with open("boyerMoore.txt", "w") as file:
        for i in range(len(title_list)):
            file.write("Title: " + title_list[i] + "\n")
            file.write("Sentiment: " + sentiment_list[i] + "\n")
            file.write("\n")


driverBM(clean_titles)
