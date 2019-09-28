'''
# 1 [Easy]

asked by Google

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

'''


#Return True if pair adds up to 1

def check_sum(a,k):
	b = set(a)
	for i in a:
		if k-i in b:
			print(True)
	return False

check_sum([1,2,5,3,7,7,8], 9)
