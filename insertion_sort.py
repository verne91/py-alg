#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Insertion Sort ---- Non-descending order
def insertion_sort(A):
	'''input:
			A : a list of integers
	   output:
			a sorted list with non-descending order
			'''
	for j in xrange(1,len(A)):
		key = A[j]
		i = j - 1							#insert A[j] into sorted sequence A[1...j-1]
		while i > 0 and A[i] > key:
			A[i+1] = A[i]
			i -= 1
		A[i+1] = key
	return A
	
if __name__ == '__main__':
	a = [1,3,5,3,89,5,44,2]
	insertion_sort(a)
	print a
