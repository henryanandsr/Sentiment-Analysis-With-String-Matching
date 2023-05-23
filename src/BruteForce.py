import nltk
from nltk.corpus import opinion_lexicon

nltk.download('opinion_lexicon')

positive_words = set(opinion_lexicon.positive())
negative_words = set(opinion_lexicon.negative())

clean_titles = []
with open("transformed_text.txt", "r") as file:
    lines = file.readlines()
    clean_titles.extend(lines)

def driverBF(titles):
    with open("BruteForce.txt", "w") as output_file:
        for title in titles:
            title = title.replace(",", "").replace(".", "")
            words = title.split()

            sentiment_score = 0
            for word in words:
                if word in positive_words:
                    sentiment_score += 1
                elif word in negative_words:
                    sentiment_score -= 1

            if sentiment_score > 0:
                sentiment = "Positive"
            elif sentiment_score < 0:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            output_file.write("Title: " + title + "\n")
            output_file.write("Sentiment: " + sentiment + "\n")
            output_file.write("\n")
            print("Title:", title)
            print("Sentiment:", sentiment)

driverBF(clean_titles)
