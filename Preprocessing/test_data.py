import csv
import numpy as np
import ast


def read_csv():
    with open("./text_embedding_student.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            string = row['vector']
            vec = np.array(ast.literal_eval(string))
            # print(np.dtype(vec[0]))
            print(vec)
            # print(row['index'], ':\n\ttype: ', type(vec), '\n\tlength: ', vec.shape, '\n\t1st entry: ', vec[0])

if __name__ == "__main__":
	read_csv()
