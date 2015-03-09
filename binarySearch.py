#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Binary search
def binary_search(aList, x):
	'''
	input:
		aList : an array with ascending order integers
		x : an integer to find in the array
	output:
		if x = aList[j], 1<=j<=n, return j
		else return 0
	'''

	low = 1
	high = len(aList)
	j = 0
	while low <= high and j == 0:
		mid = (low + high)/2
		if x == aList[mid-1]:
			j = mid
		elif x < aList[mid-1]:
			high = mid - 1
		else:
			low = mid + 1
	return j

if __name__ == '__main__':
	a = [1,4,5,6,7,8,33,77,83,87,93]
	x = 93
	y = 70
	print binary_search(a, x)
	print binary_search(a, y)
