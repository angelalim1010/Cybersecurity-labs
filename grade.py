#enter a value from keyboard: grade
#convert it to 4 scale: x *.4
#if grade < 0 and > 4 print invalid
#else if grade < 2 print F
# else if grade >= 3.7 print A and A+
#else if grade < 3.7 and grade >= 3 A-
# pass

grade = input("Please enter your grade: ")
#grade = int(input("Please enter your grade: "))
new_grade = float(grade) * .04
#new_grade = grade * .04
if new_grade < 0 or new_grade > 4: 
	print "Invalid"
elif new_grade < 2:
	print "F"
elif new_grade >= 3.7:
	print "Excellent"
elif new_grade < 3.7 and new_grade >= 3.0:
	print "Good"
else:
	print "Pass"


