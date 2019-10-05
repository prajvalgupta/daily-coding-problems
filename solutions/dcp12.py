'''
#12 [Hard]

asked by Amazon

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

'''
nWays = 0

def uniqueWays(rn): #rn represents the remaining number of steps
	global nWays
	
	if rn == 0:
		nWays += 1
		return

	uniqueWays(rn-1)

	if rn>=2:
		uniqueWays(rn-2)


def customUniqueWays(rn, posSteps):

	global nWays

	if rn==0:
		nWays+=1
		return

	for i in posSteps:
		if rn>=i:
			customUniqueWays(rn-i,posSteps)



N=4
uniqueWays(N)
print("The number of ways to climb {} stairs are {}".format(N,nWays))

posSteps = [1,3,5] # posSteps are the possible steps
nWays = 0

customUniqueWays(N,posSteps)

print("The number of ways to climb {} stairs for given possible steps {} are {}".format(N,posSteps,nWays))





