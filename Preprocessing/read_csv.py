import csv
import re
import numpy as np


def parse_csv():
	result = dict()
	with open('./data/output_csv.csv', 'r') as csv_file:
		reader = csv.DictReader(csv_file)
		for i, row in enumerate(reader):
			filename = row['Student_files']
			file_list = filename.split(',')
			res = [k for k in file_list if 'abstract' in k.lower()]
			if(len(res) < 1):
				res = [k for k in file_list if 'abs' in k.lower()]
			if(len(res) < 1):
				res = file_list
			# if(len(res) < 1):
			# 	print(i, ': ', row['Student_files'])
			name = res[0].split('\\')[-1][:-4]
			result[i] = name
			# print(i, ': ', row['Area of Research'],'\nfilename: ',  row['Student_files'])
	return result


def parse_label():
    label_count = refine_label()
    result = dict()
    with open('./data/label.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for i, row in enumerate(reader):
            labels = row['Label']
            label_list = labels.split('/')
            temp = []
            for label in label_list:
                l = label.lower()
                temp.append(label_count[l])
            
            l = label_list[temp.index(max(temp))].lower()

            if label_count[l] < 6:
                l = "others"
            if l == "":
                l = "others"
            # if l == "":
            #     l = "others"
            # if l == "remote sensing":
            #     l = "communications"
            # if l == "data mining" or l == "localization" or l == "image processing":
            #     l = "machine learning"
            # if l == "optoacoustic" or l == "optoelectronic" or l == "fiber" or l == "laser" or l == "photonics":
            #     l = "optical"
            # if l == "plasmonic":
            #     l = "quantum"
            # if l == "energy":
            #     l = "power"

            # first_label = label_list[0]
            # # first_label = re.sub(r'\W+', '', first_label)
            # first_label = first_label.lower()

            result[i] = l
    return result

def refine_label():
    result = []
    with open('./data/label.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for i, row in enumerate(reader):
            labels = row['Label']
            label_list = labels.split('/')
            for l in label_list:
                result.append(l.lower())
    
    unique, counts = np.unique(result, return_counts=True)
    label_count = dict(zip(unique, counts))

    return label_count

if __name__ == "__main__":
    # # result = parse_csv()
    # # for i in range(len(result)):
    # #     print(i, ': ', result[i])
    # result = parse_label()
    # label_set = set()
    # for i in range(len(result)):
    #     if(result[i] not in label_set):
    #         label_set.add(result[i])
    # result_list = list(label_set)
    # result_list.sort()
    # print(len(result_list), '\n')
    # # for i in result_list:
    # #     print(i)
    # print(result_list)

    # res = refine_label()
    # print(len(res))
    # for k in res:
    #     print(k, res[k])

    res = parse_label()
    temp = []
    for k in res:
        temp.append(res[k])
    temp = set(temp)
    temp = list(temp)

    print(temp)