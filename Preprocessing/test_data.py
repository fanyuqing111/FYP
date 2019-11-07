import csv
import numpy as np
import ast
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def read_csv():
    tot = np.empty(shape=[0,128])
    label_list = []
    with open("./text_embedding_student.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            string = row['vector']
            vec = np.array(ast.literal_eval(string))
            tot = np.vstack((tot, vec))
            label = row['label']
            label_list.append(label)

    # print(tot.shape)
    df = pd.DataFrame(tot, index=range(tot.shape[0]), columns=range(tot.shape[1])) # dtype: float64
    columns = ["dim_"+str(i+1) for i in range(128)]
    df.columns = columns
    label_df = pd.DataFrame(label_list)
    df.insert(1, "label", label_df)
    return df

if __name__ == "__main__":
    df = read_csv()
    vec_columns = ["dim_"+str(i+1) for i in range(128)]
    x = df.loc[:, vec_columns].values
    y = df.loc[:, ['label']].values

    x = StandardScaler().fit_transform(x)
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(x)
    principalDF = pd.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2'])
    finalDf = pd.concat([principalDF, df[['label']]], axis = 1)

    # principalDF.plot(kind='scatter', x='principal component 1', y='principal component 2', color='red')
    # plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('Principal Component 1', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    ax.set_title('2 component PCA', fontsize = 20)

    labels = ['battery', 'communications', 'others', 'power', 'signal', 'circuit', 'optical', 'control', 'materials', 'machine learning']
    colors = cm.rainbow(np.linspace(0, 1, len(labels)))

    for label, color in zip(labels, colors):
        indicesToKeep = finalDf['label'] == label
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , color = color
               , s = 50)
    ax.legend(labels)
    ax.grid()
    plt.show()