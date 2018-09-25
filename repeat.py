#Enter an integer value 'n'
#repeat 'n' if 'n<0'
#print 'n'

n = int(input("Please enter a value: "))

while n < 0:
	print "You've entered a negative number"
	n = int(input("Please enter a new value: "))
print "The number you have entered is" , n
