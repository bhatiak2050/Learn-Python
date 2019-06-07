marks = 90
grade = object()
if marks >= 90:
        print("Your grade is A")
        grade = 'A'
elif marks < 90 and marks >= 80:
        print("Your grade is B")
        grade = 'B'
elif marks < 80 and marks >= 70:
        print("Your grade is C")
        grade = 'C'
elif marks < 70 and marks >= 60:
        print("Your grade is D")
        grade = 'D'
else:
        print("Your grade is F")
        grade = 'F'
print("Grade: %c" % grade)
