#!/usr/bin/env python

import sys
import itertools
import math

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
	prev = {}
	cur = {}
	for m in xrange(2, np):
		print("m=%s"%(m))
		(prev, cur) = (cur, prev)
		cur.clear()
		for s in genSet(np, m):
			l = [-sys.maxint]*np
			l[0] = 0 if len(s) == 1 and 1 in s else sys.maxint
			cur[s] = l
			for j in s:
				if j != 1:
					l[j-1] = min(prev, s, j, points)

	m = sys.maxint
	for j in xrange(2, np+1):
		d = cur[frozenset(xrange(1, np+1))] + dist(points, j, 1)
		if d < m:
			m = d
	return m

					
def min(A, s, j, points):
	m = sys.maxint
	for k in s:
		if k != j:
			d = A[s - frozenset([j])][k-1] + dist(points, j, 1)
			if d < m:
				m = d
	return m

def dist(points, j, k):
	dx = points[j-1][1] - points[k-1][1]
	dy = points[j-1][2] - points[k-1][2]
	math.sqrt(dx*dx + dy*dy)

def genSet(max, size):
	s = range(1, max+1)
	for s in itertools.combinations(s, size):
		ss = frozenset(s)
		if 1 in ss:
			yield ss

if __name__ == '__main__':
	points = readProblem('tsp.txt')
	m = calc(points)
	print('TSP %s'%(m))