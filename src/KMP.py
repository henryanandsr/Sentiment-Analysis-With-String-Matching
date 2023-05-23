import nltk
from nltk.corpus import opinion_lexicon

nltk.download('opinion_lexicon')

positive_words = set(opinion_lexicon.positive())
negative_words = set(opinion_lexicon.negative())

clean_titles = []
with open("transformed_text.txt", "r") as file:
    lines = file.readlines()
    clean_titles.extend(lines)

def compute_prefix(pattern):
    prefix = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix[i] = j
    return prefix

def kmp_search(text, pattern):
    prefix = compute_prefix(pattern)
    matches = []
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            matches.append(i - j + 1)
            j = prefix[j - 1]
    return matches

def driverKMP(titles):
    title_list = []
    sentiment_list = []
    for title in titles:
        title = title.lower()
        title = title.replace(",", "").replace(".", "")
        words = title.split()

        sentiment_score = 0
        for word in words:
            if any(kmp_search(word, positive_word) for positive_word in positive_words):
                sentiment_score += 1
            elif any(kmp_search(word, negative_word) for negative_word in negative_words):
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


    with open("KMP.txt", "w") as file:
        for i in range(len(title_list)):
            file.write("Title: " + title_list[i] + "\n")
            file.write("Sentiment: " + sentiment_list[i] + "\n")
            file.write("\n")


driverKMP(clean_titles)
