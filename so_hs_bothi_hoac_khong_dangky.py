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

#number of students who took subjects
num_of_exam_taken = [0,0,0,0,0,0,0,0,0,0]
average = [0,0,0,0,0,0,0,0,0,0]

for student in students:
	count = 0
	total = 0
	for i in range(9):
		if student[i+1] != "-1":
			total += float(student[i+1]) 
			count += 1

	num_of_exam_taken[count] += 1
	if count != 0:
		average[count] += total/count
for i in range(10):
	if num_of_exam_taken[i]!=0:
		average[i] = round(average[i]/num_of_exam_taken[i], 2)

print(num_of_exam_taken)
print(average)


#plot barchart
import numpy as np
import matplotlib.pyplot as plt 


#numpy from 0-9
x_pos = np.arange(10)
y_pos = np.arange(10)

figure, axis = plt.subplots()
#plot the barchart using 2 lists
plt.bar(x_pos, average)
#change horizontal category name
plt.xticks(x_pos, y_pos)

#set limit to vertical axis
axis.set_ylim(0,10)

#label and title
plt.ylabel('Điểm trung bình')
plt.title('Điểm trung bình theo số lượng môn thi')

#draw number of student on top of each bar
rects = axis.patches
for rect, label in zip(rects, average):
	height = rect.get_height()
	axis.text(rect.get_x() + rect.get_width() / 2, height, label, ha='center', va='bottom')

#show the plot
plt.show()