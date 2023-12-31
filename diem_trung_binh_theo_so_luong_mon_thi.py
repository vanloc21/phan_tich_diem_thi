#read file
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


not_take_exam = [0,0,0,0,0,0,0,0,0]


#loop through all students
for student in students:
	#iterate through all subjects
	for i in range(1,10):
		if student[i] == "-1":
			not_take_exam[i-1] += 1


not_take_exam_percentage = [0,0,0,0,0,0,0,0,0]

for i in range(0,9):
	not_take_exam_percentage[i] = round(not_take_exam[i]*100/total_student, 2)
print(not_take_exam_percentage)


#plot barchart
import numpy as np
import matplotlib.pyplot as plt 

figure, axis = plt.subplots()

#numpy from 0-9
y_pos = np.arange(len(subjects))

#plot the barchart using 2 lists
plt.bar(y_pos, not_take_exam_percentage)
#change horizontal category name
plt.xticks(y_pos, subjects)

#set limit to vertical axis
axis.set_ylim(0,120)

#label and title
plt.ylabel('Percentage')
plt.title('Số học sinh bỏ thi hoặc không đăng kí')

#draw number of student on top of each bar
rects = axis.patches
for rect, label in zip(rects, not_take_exam):
	height = rect.get_height()
	axis.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')

#show the plot
plt.show()
