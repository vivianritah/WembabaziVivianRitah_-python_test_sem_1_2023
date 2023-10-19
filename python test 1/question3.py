#list
student_marks=[78, 83, 90, 88, 75]
sum_of_student_marks= 78+83+90+75
print("The sum of the items in student marks list is " + str(sum_of_student_marks))

#display
first_mark= student_marks[0]
last_mark= student_marks[4]
print("first mark", first_mark)
print("last mark", last_mark)

#add
student_marks.append(96)
print(student_marks)

#update
student_marks[0]=87
print(student_marks)
