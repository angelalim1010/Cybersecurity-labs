
# 1. print max interge in Python

import sys
max = sys.maxsize
min = -sys.maxsize - 1
print (max)
print (min)

# introduce package and namespace

# 2. Complete your code:

age = int(input("Enter your age: "))

# the following code is incomplete

if age >= 0 and age < 13: 
	print("You are child.")
elif age >= 13 and age <= 18:
	print("You are teenager.")
elif age >= 19 and age <= 64:
	print("You are an adult")
elif age >= 65 and age <= 120:
	print("You are a senior")
else:
	print("You are an alien")
# 3. Correct the code:
numbers = [0] * 10
print(numbers)

for i in range(10):
	numbers[i] = i
print(numbers)


# 4. encode and decode
# only consider lower case
# encode

password = raw_input("Enter your password: ")
newPassword = ""
for i in range(len(password)):
	if (ord(password[i]) + 1 <= ord('z')):
		newPassword += chr(ord(password[i]) + 1)
	else:
		newPassword += "a"
print(newPassword)


# decode
password = raw_input("Enter your encoded password: ")
newPassword = ""
for i in range(len(password)):
	if (ord(password[i]) - 1 >= ord('a')):
		newPassword += chr(ord(password[i]) - 1)
	else:
		newPassword += "z"
print(newPassword)
