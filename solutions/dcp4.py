'''
#4 [Hard]
asked by Stripe

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

'''

def missing_integer(array):

	n = len(array)
	if n == 0:
		return 1
	for i in range(n):
		if array[i] <= 0 or array[i] > n:
			array[i] = n + 1
			# print(array)
			# print("-------")
	for i in range(n):
		if abs(array[i]) == n + 1:
			continue
		array[abs(array[i])-1] = - abs(array[abs(array[i])-1])
		# print(array)
		# print("++++++++")
	for j in range(n):
		if array[j] > 0:
			return j + 1
	return n + 1


a = missing_integer([3,4,-1,1])
print(a)