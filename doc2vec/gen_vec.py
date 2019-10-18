from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import sys
sys.path.insert(1, '/Users/pangyujin/Development/FYP_project')
from Preprocessing.preprocess import normalize_string


def doc2vec(doc):
    # train model from common_texts
    documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(common_texts)]
    model = Doc2Vec(documents, vector_size=5, window=2, min_count=1, workers=4)
    model.delete_temporary_training_data(keep_doctags_vectors=True, keep_inference=True)
    # generate vector
    vector = model.infer_vector(doc)
    return vector


if __name__ == "__main__":
	with open("/Users/pangyujin/Development/FYP_project/Preprocessing/school_project_test_file/student_folder/publication_1_.txt", "r") as f:
	    input_string = normalize_string(f.read())
	    doc_list = input_string.split()
	    res = doc2vec(doc_list)
	    print(res)