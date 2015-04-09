#!/usr/bin/env python

import sys

FILE = 'clustering1.txt'

class Point(object):
	def __init__(self, num):
		self.num = num
		self.parent = self
		self.size = 1

	def __repr__(self):
		return 'Point(%s)'%(self.num)

class Edge(object):
	def __init__(self, a, b, dist):
		self.dist = dist
		self.a = a
		self.b = b

	def __repr__(self):
		return 'Edge(%s, %s, %s)'%(self.a, self.b, self.dist)

def find(p):
	if (p.parent is p):
		return p
	else:
		return find(p.parent)

def union(p1, p2):
	r1 = find(p1)
	r2 = find(p2)
	if (r1 is r2):
		return False
	if (r2.size > r1.size):
		(r1, r2) = (r2, r1)
	r1.size += r2.size
	r2.size = None
	r2.parent = r1
	return True

def algo(edges, numPoints, target):
	clusters = numPoints
	edges.sort(key=lambda e: e.dist)
	for e in edges:
		if (union(e.a, e.b)):
			clusters -= 1
			if clusters < target:
				return e.dist
	return None

def readEdges():
	points = {}
	edges = []
	def node(num):
		if (num not in points):
			points[num] = Point(num)
		return points[num]

	with open(FILE, 'r') as f:
		num = int(f.readline())
		for l in f.readlines():
			lineValues = map(int, l.split())
			a = node(lineValues[0])
			b = node(lineValues[1])
			edges.append(Edge(a, b, lineValues[2]))
	return (num, edges)

if __name__ == '__main__':
	(numNodes, edges) = readEdges()
	print(algo(edges, numNodes, 4))
