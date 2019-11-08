import csv
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
sys.path.insert(1, '/Users/pangyujin/Development/FYP_project')
from Preprocessing.preprocess import normalize_string
from collections import Counter


def keyword_corpus():
    corpus = []
    with open('./data/label.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for i, row in enumerate(reader):
            thesis = normalize_string(row['Title of Thesis'])
            area = normalize_string(row['Area of Research'])
            text = thesis + ' ' + area
            corpus.append(text)
    return corpus

if __name__ == "__main__":
    corpus = keyword_corpus()
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    # print(len(vectorizer.get_feature_names()))
    words = vectorizer.get_feature_names()
    # print(X.getrow(0))

    
    key_words_index = []
    for i in range(X.shape[0]):
        newrow = X.getrow(i)
        row_dict = dict()
        row_index = []
        for row, col in zip(*newrow.nonzero()):
            row_dict[col] = newrow[row, col]
        top_5 = dict(Counter(row_dict).most_common(5))
        for key in top_5:
            row_index.append(key)
        key_words_index.append(row_index)

    with open("./myCorpus/keywords.csv", "w+") as csv_file:
        fieldnames = ["index", "keywords"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i, indexs in enumerate(key_words_index):
            new_line = ','.join([words[j] for j in indexs])
            writer.writerow({"index": i, "keywords": new_line})

    print("keywords saved into file")