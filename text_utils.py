
import re
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Download required NLTK resources
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)


# Initialize NLP tools
stop_words = set(stopwords.words("english"))

# Preserve important negative words
stop_words.discard("not")
stop_words.discard("no")
stop_words.discard("nor")

lemmatizer = WordNetLemmatizer()


# Text cleaning function
def clean_text(text):

    if not isinstance(text, str):
        text = str(text)

    # Convert to lowercase
    text = text.lower()

    # Remove numbers
    text = re.sub(r"\d+", " ", text)

    # Remove special characters
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Tokenization
    tokens = word_tokenize(text)

    # Remove stopwords and lemmatize
    cleaned_tokens = []

    for word in tokens:

        if word not in stop_words:

            lemma = lemmatizer.lemmatize(word)

            cleaned_tokens.append(lemma)

    return " ".join(cleaned_tokens)
