data_valid = False

while data_valid == False:
    grade1 = float ( input("Type the grade of your first test: ") )
    if grade1 < 0 or grade1 > 10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    grade2 = float ( input("Type the grade of your second test: ") )
    if grade2 < 0 or grade2 > 10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    total_classes = int ( input("Type the total number of classes: ") )
    if total_classes <= 0:
        print("Enter the number of classes you attended. It must be a figure")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    absences = int(input("Type many times have you been absent: "))
    if absences <= -1 or absences > total_classes:
        print("Enter number of times you were absent. It must be a figure less than number of total classes")
        continue
    else:
        data_valid = True

avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absences) / total_classes
print("Average grade: ", round(avg_grade, 2))
print("Attendance: ", str(round((attendance * 100),2))+"%")

if (avg_grade>= 6):
    if (attendance>= 0.8):
        print("You passed!")
    else:
        print("You failed because you attended less than 80% of lectures!")
elif (attendance>= 0.8):
    print ("You failed because your score average is less than 6 out of 10")
else:
    print("You failed because you got less than 6 and attended less than 80% of the lectures!")