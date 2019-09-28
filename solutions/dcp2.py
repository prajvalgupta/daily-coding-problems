
'''
# 2 [Hard]

asked by Uber

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

'''
a=[1, 2, 3, 4, 5]

b=[]

for i in range(len(a)):
	x=1
	for j in range(len(a)):
		if j!=i:
			x=x*a[j]
	b.append(x)
	print(b)

