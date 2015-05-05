#!/usr/bin/env python

import sys

FILE = 'knapsack_big.txt'

class Item(object):
	def __init__(self, v, w):
		self.v = v
		self.w = w

	def __repr__(self):
		return 'I(value=%s, weight=%s)'%(self.v, self.w)

def readProblem():
	items = []
	with open(FILE, 'r') as f:
		h = map(int, f.readline().split())
		size = h[0]
		num = h[1]
		for l in f.readlines():
			il = map(int, l.split())
			items.append((il[0], il[1]))
	return (size, items)

def calc(size, items):
	ni = len(items)
	src = [-1]*(size+1)
	dst = [-1]*(size+1)

	for x in xrange(0, size+1):
		src[x] = 0
	for i in xrange(1, ni+1):
		if (i % 10 == 0):
			print('%s done'%(i))
		it = items[i-1]
		for x in xrange(0, size+1):
			if it[1] <= x:
				dst[x] = max(src[x], src[x-it[1]]+it[0])
			else:
				dst[x] = src[x]
		src, dst = dst, src
	return src[size]

if __name__ == '__main__':
	(size, items) = readProblem()
	print(calc(size, items))
