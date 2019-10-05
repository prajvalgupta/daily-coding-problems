'''
#13 [Hard]

asked by Amazon

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

'''

#This is the O(n^2) solution. 

def longestSubstring(s,k):

	b = []
	for i in range(len(s)-1):
		for j in range(i+1,len(s)-1):
			a = s[i:j+1]
			if len(set(a)) <=2:
				b.append(a)
				# print(b)
	return max(b, key=len)


b = longestSubstring("abcba",2)
print(b)