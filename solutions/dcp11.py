'''
#11 [Medium]

asked by Twitter


Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

'''

import re

def matchString(s,array):
	r = re.compile(s)
	newList = list(filter(r.match,array))

	return newList


array = ["dog", "deer", "deal"]
s = "de"
print(matchString(s,array))
