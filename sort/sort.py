#!/usr/bin/env python

FILE_NAME="QuickSort.txt"
#FILE_NAME="test.txt"

def quicksort(array, left, right, pivot):
	if left>=right:
		return 0
	p = pivot(array, left, right)
	x = array[p]
	array[p]=array[left]
	array[left]=x
	pos = partition(array, left, right)
	l = quicksort(array, left, pos-1, pivot)
	r = quicksort(array, pos+1, right, pivot)
	return (right-left) + l + r

def partition(array, left, right):
	p = array[left]
	i = left+1
	for j in range(left+1, right+1):
		if array[j] < p:
			swap(array, i, j)
			i = i+1
	swap(array, left, i-1)
	return i-1

def swap(array, i, j):
	if i!=j:
		x = array[i]
		array[i]=array[j]
		array[j]=x

def read_array(filename):
	with open(filename, 'r') as f:
		strings = f.readlines()
		ints = map(int, strings)
		return ints

def midOfThree(array, left, right):
	l = right - left + 1
	if l%2 == 0:
		m = l/2
	else:
		m = (l/2)+1
	mid = left+m-1
	if (array[left]>=array[right] and array[left]<=array[mid]) or (array[left]<=array[right] and array[left]>=array[mid]):
		return left
	if (array[right]>=array[left] and array[right]<=array[mid]) or (array[right]<=array[left] and array[right]>=array[mid]):
		return right
	
	return mid

if __name__ == "__main__":
	array = read_array(FILE_NAME)

	cmpFirst = quicksort(list(array), 0, len(array)-1, lambda a,l,r: l)
	cmpLast = quicksort(list(array), 0, len(array)-1, lambda a,l,r: r)
	cmpMid = quicksort(list(array), 0, len(array)-1, midOfThree)
	print cmpFirst
	print cmpLast
	print cmpMid
