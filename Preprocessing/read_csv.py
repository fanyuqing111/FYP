import csv


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

if __name__ == "__main__":
	result = parse_csv()
	for i in range(len(result)):
		print(i, ': ', result[i])
