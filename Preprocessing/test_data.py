import csv
import numpy as np
import ast
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def read_csv():
    tot = np.empty(shape=[0,128])
    with open("./text_embedding_student.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            string = row['vector']
            vec = np.array(ast.literal_eval(string))
            tot = np.vstack((tot, vec))

    # print(tot.shape)
    df = pd.DataFrame(tot, index=range(tot.shape[0]), columns=range(tot.shape[1])) # dtype: float64
    return df

if __name__ == "__main__":
    df = read_csv()
    df_x = StandardScaler().fit_transform(df)
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(df_x)
    principalDF = pd.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2'])
    
    principalDF.plot(kind='scatter', x='principal component 1', y='principal component 2', color='red')
    plt.show()
