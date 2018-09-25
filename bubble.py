a = [6,4,3,7,2,5,1]
print(a)
for i in range(6):
	for j in range(len(a) - i -1):
		if (a[j] > a[j+1]):
			temp = a[j]
			a[j] = a[j+1]
			a[j+1] = temp
	print(a)
