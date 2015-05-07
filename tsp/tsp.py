#!/usr/bin/env python

import sys
import itertools
import math
#https://code.google.com/p/yappi/wiki/usageyappi_v092
#import yappi

def readProblem(fileName):
	points = []
	with open(fileName, 'r') as f:
		cnt = int(f.readline())
		i = 1
		for l in f.readlines():
			il = map(float, l.split())
			points.append((i, il[0], il[1]))
			i+=1
		if len(points)!=cnt:
			raise Exception("Mismatch on counts")
	return points

def calc(points):
	np = len(points)
	cache = [frozenset([x]) for x in xrange(1, np+1)]
	prev = {}
	cur = {}
	initS = frozenset([1])
	prev[initS] = array(np, initS)
	for m in xrange(2, 8):
		print("m=%s"%(m))
		cur.clear()
		for s in genSet(np, m):
			l = array(np, s)
			cur[s] = l
			for j in s:
				if j != 1:
					l[j-1] = min(prev, s, j, points, cache)
		(prev, cur) = (cur, prev)

	m = sys.maxint
	for j in xrange(2, np+1):
		d = prev[frozenset(xrange(1, np+1))] + dist(points, j, 1)
		if d < m:
			m = d
	return m

def array(np, s):
	l = [-sys.maxint]*np
	l[0] = 0 if len(s) == 1 and 1 in s else sys.maxint
	return l
					
def min(A, s, j, points, cache):
	m = sys.maxint
	for k in s:
		if k != j:
			d = A[s - cache[j-1]][k-1] + dist(points, k, j)
			if d < m:
				m = d
	return m

def dist(points, j, k):
	a = points[j-1]
	b = points[k-1]
	dx = a[1] - b[1]
	dy = a[2] - b[2]
	return math.sqrt(dx*dx + dy*dy)

def genSet(max, size):
	s = range(1, max+1)
	for s in itertools.combinations(s, size):
		ss = frozenset(s)
		if 1 in ss:
			yield ss

if __name__ == '__main__':
	points = readProblem('tsp.txt')
	#yappi.start()
	m = calc(points)
	#yappi.get_func_stats().print_all()
	print('TSP %s'%(m))

