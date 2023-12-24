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

#number of students who score from 1-10 of any subjects
num_of_student_subject = [0] * 51
scores_spectrum = [round(i/10, 1) for i in range(0, 101, 2)]
print(students[0])

count = 0
for student in students:
	x = round(float(student[1]),2)
	if x != -1:
		count += 1
		if x < 10:
			for i in range(len(scores_spectrum)-1):
				if scores_spectrum[i] <= x < scores_spectrum[i+1]:
					num_of_student_subject[i] += 1
					break
		else:
			num_of_student_subject[-1] += 1
		

print(count)
print(num_of_student_subject)

diemtb = 0
for i in range(len(scores_spectrum)):
	diemtb = diemtb + (scores_spectrum[i]*num_of_student_subject[i])
print(round(diemtb/count, 2))


#plot barchart
import numpy as np
import matplotlib.pyplot as plt 

figure, axis = plt.subplots()

#numpy from 0-9
y_pos = np.arange(len(scores_spectrum))

#plot the barchart using 2 lists
plt.bar(y_pos, num_of_student_subject)
#change horizontal category name
plt.xticks(y_pos, scores_spectrum, rotation=90)

#set limit to vertical axis
#axis.set_ylim(0,120)

#label and title
plt.ylabel('Số lượng thí sinh')
plt.title('Biểu đồ phổ điểm thi THPT Toán cụm Đà Nẵng - năm 2023 ')

#draw number of student on top of each bar
rects = axis.patches
for rect, label in zip(rects, num_of_student_subject):
	height = rect.get_height()
	axis.text(rect.get_x() + rect.get_width()/2 , height + 5, label, ha='center', va='bottom', rotation=90)

#show the plot
plt.show()
