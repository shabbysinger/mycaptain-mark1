a1 = 0
a2 = 1
max = int(input('Enter the max number of terms: '))
for i in range(max):
	print(a1)
	temp = a1
	a1 = a1 + a2
	a2 = temp
