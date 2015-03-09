#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Merge two sorted array into one.
def merge(A, B):
	'''
	input:
		A, B : a list of sorted integers with non-descending order
	output:
		a merged list with non-descending order
	'''

	temp = []
	s = 0
	t = 0
	while s < len(A) and t < len(B):
		if A[s] <= B[t]:
			temp.append(A[s])
			s += 1
		else:
			temp.append(B[t])
			t += 1
	if s == len(A):
		temp += B[t:]
	else:
		temp += A[s:]
	return temp

if __name__ == "__main__":
	A = [1,2,5]
	B = [3,4,6,9,10]
	print merge(A,B)
