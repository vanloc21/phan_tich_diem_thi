#read file2
with open("clean_data.csv", encoding="utf8") as file:
	data = file.read().split("\n")

header = data[0]
students = data[1:]

#remove last student (empty student)
students.pop()

total_student = len(data)

#split header
header = header.split(",")
subjects = header[1:]


#split each student in list
for i in range(len(students)):
	students[i] = students[i].split(",")

#number of students who took subjects
num_of_exam_taken = [0,0,0,0,0,0,0,0,0,0]

for student in students:
	count = 0
	for i in range(9):
		if student[i+1] != "-1":
			count += 1


	num_of_exam_taken[count] += 1

print(num_of_exam_taken)

import matplotlib.pyplot as plt

#pie chart, where the slices will be ordered and plotted counter-clockwise
labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
sizes = [99, 12, 17, 316, 1194, 452, 11043, 0, 0, 0]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal') #Equal aspect ratio ensures that pie is 

plt.show()

