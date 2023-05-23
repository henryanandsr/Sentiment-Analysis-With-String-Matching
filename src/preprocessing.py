import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def text_transformation(text):
    new_text = re.sub('[^a-zA-Z]', ' ', text)
    new_text = new_text.lower()
    new_text = new_text.split()
    new_text = [lemmatizer.lemmatize(word) for word in new_text if word not in set(stopwords.words('english'))]
    transformed_text = ' '.join(new_text)
    return transformed_text

nltk.download('stopwords')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

with open("list_judul.txt", "r") as file:
    lines = file.readlines()

corpus = []
for line in lines:
    transformed_line = text_transformation(line)
    corpus.append(transformed_line)

for transformed_text in corpus:
    print(transformed_text)
    with open("transformed_text.txt", "a") as file:
        file.write(transformed_text + "\n")
