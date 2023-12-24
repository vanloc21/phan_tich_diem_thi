import csv

file = open("a.txt", "r")

#Read first student
datas = file.read().split("\n")

with open("clean_data.csv", encoding="utf8",  mode="w", newline='') as file_csv:
	header = ["sbd", "toán", "ngữ văn", "lịch sử", "địa lí", "giáo dục công dân", "sinh học", "vật lý", "hóa học", "ngoại ngữ"] 
	writer = csv.writer(file_csv)
	writer.writerow(header)

for data in datas:
	#make data becomes a list
	data  = data.split("\\n")

	#remove \r & \t
	for i in range(len(data)):
		data[i] = data[i].replace("\\r", "")
		data[i] = data[i].replace("\\t", "")

	#remove tags1
	tags = []
	for i in range(len(data)):
		tags = []
		for j in range(len(data[i])):
			if data[i][j]=="<":
				begin = j
			if data[i][j]==">":
				end = j
				tags.append(data[i][begin:end+1])
		for tag in tags:
			data[i] = data[i].replace(tag, "")

	#removes leading whitespace
	for i in range(len(data)):
		data[i] = data[i].strip()

	#remove empty line
	unempty_lines = []
	for i in range(len(data)):
		if data[i] != "":
			unempty_lines.append(data[i])
	data = unempty_lines


	#choose relevance info
	idx_sbd = data.index(r"Chi ti\xe1\xba\xbft th\xc3\xad sinh") + 1
	sbd = data[idx_sbd]	
	idx = data.index("\\xc4\\x90i\\xe1\\xbb\\x83m") + 1
	scores=""
	while data[idx]!='googTagCode.display.push("sis_large1");':
		scores = scores + (str(data[idx]) + "  ")
		idx += 1

	#load unicode table
	chars = []
	codes = []	
	file = open("unicode.txt", encoding="utf8")
	unicode_table = file.read().split("\n")

	for code in unicode_table:
		x = code.split(" ")
		chars.append(x[0])
		codes.append(x[1])

	#replace special characters in scores
	for i in range(len(chars)):
		#sbd = sbd.replace(codes[i], chars[i])
		scores = scores.replace(codes[i], chars[i])

	for i in range(len(scores)):
		if scores[i:i+2] == "&#":
			scores = scores[:i] + chr(int(scores[i+2:i+5])) + scores[i+5:]

	#change to lower case
	sbd = sbd.lower()
	scores = scores.lower()

	#process sbd
	sbd = sbd.replace("s\\xe1\\xbb\\x91 b\\xc3\\xa1o danh: ", "")

	#process scores
	scores_list = scores.split("  ")
	#print(scores_list)

	data = [sbd]

	#add score to data
	for subject in ["toán", "ngữ văn", "lịch sử", "địa lý", "giáo dục công dân", "sinh học", "vật lý", "hóa học", "ngoại ngữ"]:
		if subject in scores_list:
			data.append(str(float(scores_list[scores_list.index(subject)+1])))
		else:
			data.append("-1")

	with open("clean_data.csv", "a", encoding='utf-8', newline='') as file_csv:
		writer = csv.writer(file_csv)
		writer.writerow(data)


