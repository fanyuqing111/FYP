#!/usr/local/anaconda3/bin/python3
import re
import string
import nltk
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
nltk.download('words')
nltk.download('punkt')
nltk.download('wordnet')


def read_file():
    with open("./school_project_test_file/student_folder/publication_1_.txt", "r") as f:
        data = f.read()
        return data


def filter_ascii(inp_str):
    inp_str = inp_str.lower()
    
    # remove line breaks
    inp_str = re.sub(r"(\n+)", ' ', inp_str)
    # remove all numbers
    inp_str = re.sub(r"(\d+)", ' ', inp_str)
    # remove non-ascii
    inp_str = re.sub(r'[^\x00-\x7F]+', ' ', inp_str)
    # remove punctuation
    # translator = str.maketrans('','',string.punctuation)
    # inp_str = inp_str.translate(translator)
    inp_str = re.sub('['+string.punctuation+']', ' ', inp_str)
    # remove all single character
    inp_str = re.sub(r"(\b\w\b)", ' ', inp_str)
    # replace multi spaces into one
    inp_str = re.sub(r"(\s+)", ' ', inp_str)
    inp_str = inp_str.strip()

    # stemming & lemmatizing
    from nltk.stem import PorterStemmer
    from nltk.stem import WordNetLemmatizer
    from nltk.tokenize import word_tokenize
    lemmatizer=WordNetLemmatizer()
    stemmer= PorterStemmer()
    inp_str = word_tokenize(inp_str)
    # for word in inp_str:
    #     print(word + "-> " + lemmatizer.lemmatize(word))
    inp_str = list(map((lambda x: lemmatizer.lemmatize(x)), inp_str))
    # inp_str = list(map((lambda x: stemmer.stem(x)), inp_str))
    inp_str = ' '.join(inp_str)

    return inp_str


if __name__ == '__main__':
    data = read_file()
    res = filter_ascii(data)

    # # detect stop words
    # from nltk.tokenize import word_tokenize
    # tokens = word_tokenize(res)
    # res = ' '.join([i for i in tokens if not i in ENGLISH_STOP_WORDS])

    # detect if word is in english
    # english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    # for word in res.split():
    #     if(word in english_vocab):
    #         print(word + ': ' + 'True')
    #     else:
    #         print(word + ': ' + 'False')
    
    print(res)
