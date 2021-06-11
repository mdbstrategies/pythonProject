grade1 = float ( input("Type the grade of your first test: ") )
grade2 = float ( input("Type the grade of your second test: ") )
absences = int ( input("Type many times have you been absent: "))
total_classes = int ( input("Type the total number of classes: "))

avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absences) / total_classes

print("Average grade: ", round(avg_grade, 2))
print("Attendance: ", str(round((attendance * 100),2))+"%")

if (avg_grade>= 6 and attendance>= 0.8):
        print("You passed!")
elif (avg_grade < 6 and attendance < 0.8):
    print("You failed because you got less than 6 and attended less than 80% of the lectures!")
elif (attendance >= 0.8):
    print("You failed because your score average is less than 6 out of 10")
else:
    print("You failed because you attended less than 80% of lectures!")


