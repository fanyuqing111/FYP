from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import csv
import numpy as np
import sys
sys.path.insert(1, '/Users/pangyujin/Development/FYP_project')
from Preprocessing.preprocess import normalize_string
from Preprocessing.read_csv import parse_csv, parse_label
from Preprocessing.myCorpus.training_data import load_corpus


def generate_vector(model, doc):
    # generate vector
    vector = model.infer_vector(doc)
    return vector


if __name__ == "__main__":
    DATA_FOLDER = "/Users/pangyujin/Development/FYP_project/Preprocessing/data"

    # train model from own dataset
    my_corpus = load_corpus()
    documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(my_corpus)]
    model = Doc2Vec(documents, vector_size=128, min_count=1, dm=1, window=10, workers=4)
    model.delete_temporary_training_data(keep_doctags_vectors=True, keep_inference=True)

    result = parse_csv()
    labels = parse_label()
    with open("text_embedding_student.csv", "w") as csv_file:
        fieldnames = ["index", "label", "vector"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(result)):
            filename = result[i] + ".txt"
            # try:
            with open(DATA_FOLDER + "/student_folder/" + filename, "r") as f:
                input_string = normalize_string(f.read())
                doc_list = input_string.split()
                vec = generate_vector(model, doc_list)
                writer.writerow({"index": i, "label": labels[i], "vector": vec.tolist()})
        print("Result has been written to file")