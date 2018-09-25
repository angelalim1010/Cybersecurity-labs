
this_year = 2018
print "This year is:", this_year
#this_year = this_year + 1
#print "This year is:", this_year

birth_year = input("Please enter your year of birth: ")
age = this_year - int(birth_year)
print "Your age is: ", age

if age >= 13 and age <=18: 
	print "Teenager"
elif age < 13: 
	print "Kid"
elif age >= 18 and age <= 55: 
	print "Adult"
else: 
	print "Senior"

