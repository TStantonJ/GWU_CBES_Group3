"""
File that provides functionality for Preprocessing string data for keyword search.
Preprocessing includes: normalization of text(capitol and non-text), tokenization of text, removal of stop word tokens, lemmatization and stemming of tokens.

Written by: Thomas Stanton
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import re

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


def preprocess_text(text):
    """
    preprocess_text converts a text into a tokenized array.

    :param text: A string text to be tokenized.
    :return: A list of strings that can be combined to represent the text without stopwords,
    stems, uppercase letters, non-alphabet chars, and where the words are lemmatized if possible.
    """
    # Normalization: convert to lowercase
    text = text.lower()

    # Non-Alpha Removal: remove non alphabet characters
    text = re.sub(r'[^0-9a-zA-Z ]+', '', text)
    print(text)

    # Tokenization: split the text into words
    tokens = word_tokenize(text)

    # Stop Words Removal: remove common words
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]

    # Stemming: reduce words to their root form
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]

    # Lemmatization: reduce words to their base or dictionary form
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in stemmed_tokens]

    return lemmatized_tokens

if __name__ == '__main__':
    # Example usage
    example_text = "TensorFlow is an end-to-end open source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries, and community resources that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML-powered applications."
    processed_text = preprocess_text(example_text)
    print(processed_text)