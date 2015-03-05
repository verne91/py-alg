#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Linear search 
def linearSearch(aList, x):
	'''input:
			aList : an array with n integers
			x : an integer to search in the array
	   output:
			if x = aList[j], 1<=j<=n, return j
			else return 0
	'''

	j = 0
	while j < len(aList) and x != aList[j]:
		j += 1
	if x == aList[j]:
		return j+1
	else:
		return 0

if __name__ == '__main__':
	a = [55,22,33,11,9,0,8]
	x = 0
	print linearSearch(a,x)
