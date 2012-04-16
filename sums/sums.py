#!/usr/bin/env python

import sys

FILE = 'HashInt.txt'
SUMS = [231552,234756,596873,648219,726312,981237,988331,1277361,1283379]
MAX = 100000

def readInts():
	ints = set()
	with open(FILE, 'r') as f:
		for l in f.readlines():
			i = int(l)
			ints.add(i)
	return ints

def isSum(sum, ints):
	for i in xrange(1, MAX/2):
		if (i in ints) and ((sum-i) in ints):
			return True
	return False

if __name__ == '__main__':
	ints = readInts()
	res = map(lambda s: isSum(s, ints), SUMS)
	print res
