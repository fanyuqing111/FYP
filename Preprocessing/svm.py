import csv
import sklearn
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
import numpy as np
import ast
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def converter(label_str):
    labels = ['', 'antenna', 'battery', 'circuit', 'communications', 'control', 'data mining', 'electromagnetic', 'energy', 'fiber', 'image processing', 'laser', 'localization', 'machine learning', 'materials', 'math', 'network', 'nmr', 'optical', 'optoacoustic', 'optoelectronic', 'photonics', 'plasmonics', 'power', 'quantum', 'remote sensing', 'security', 'signal', 'solar']
    label_map = dict()
    for i, item in enumerate(labels):
        label_map[item] = i

    return label_map[label_str]

def read_csv():
    data_ary = np.empty(shape=[0,128])
    label_list = []
    with open("./text_embedding_student.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            string = row['vector']
            vec = np.array(ast.literal_eval(string))
            data_ary = np.vstack((data_ary, vec))
            label = row['label']
            label_list.append(label)

    label_list = [converter(i) for i in label_list]
    label_ary = np.array(label_list)

    return data_ary, label_ary
    # print(data_ary.shape) # (175, 128), 175 rows of data, 128 dimension
    # print(label_list.shape) # (175, ) 175 rows of data 


if __name__ == "__main__":
    X, Y = read_csv()

    classifier=svm.SVC(C=2,kernel='rbf',gamma=10,decision_function_shape='ovr') # ovr:一对多策略

    kf = KFold(n_splits=5)
    kf.get_n_splits(X)
    i = 1
    for train_index, test_index in kf.split(X):
        # print("TRAIN:", train_index, "TEST:", test_index)
        X_train, X_test = X[train_index], X[test_index]
        Y_train, Y_test = Y[train_index], Y[test_index]
        classifier.fit(X_train, Y_train)
        print("Iteration" + str(i) + ":")
        print("Train Accuracy: ",classifier.score(X_train,Y_train))
        print("Test Accuarcy: ",classifier.score(X_test,Y_test))
        i += 1


    
    # train_data,test_data,train_label,test_label =sklearn.model_selection.train_test_split(x,y, random_state=1, train_size=0.6,test_size=0.4)

    # classifier=svm.SVC(C=2,kernel='rbf',gamma=10,decision_function_shape='ovr') # ovr:一对多策略
    # classifier.fit(train_data,train_label)

    # print("Train Accuracy: ",classifier.score(train_data,train_label))
    # print("Test Accuarcy: ",classifier.score(test_data,test_label))