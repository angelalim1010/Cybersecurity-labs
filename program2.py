testScore = int(input('Enter test score: '))
if testScore >= 90:
	print ('Your grade is A')
elif testScore >= 80:
	print('Your grade is B')
elif testScore >= 70:
	print('Your grade is C')
elif testScore >= 60:
	print('Your grade is D')
else:
	print('Your grade is F')


total = 0
print ('Please enter 10 ages: ')
for i in range(10):
	age = int(input('Please enter age: '))
	total = total + age
print('average age is ', float(total)/10)
