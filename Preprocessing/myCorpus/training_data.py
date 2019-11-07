import pickle
import os
import sys
sys.path.insert(1, '/Users/pangyujin/Development/FYP_project')
from Preprocessing.preprocess import normalize_string


def training_text():
    my_corpus = []
    for root, dirs, files in os.walk("./data"):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    file_string = normalize_string(f.read())
                    doc_list = file_string.split()
                    if(len(doc_list) > 10):
                        my_corpus.append(doc_list)

    with open("./myCorpus/my_corpus.txt", "wb") as fp:
        pickle.dump(my_corpus, fp)
    print("corpus saved")


def load_corpus():
    with open("./myCorpus/my_corpus.txt", "rb") as fp:
        corpus_list = pickle.load(fp)
        return corpus_list


if __name__ == "__main__":
    print("loaded", len(load_corpus()), "docs")
