#!/usr/bin/env python

import sys
import itertools

FILE = 'clustering_big.txt'

class Node(object):
	def __init__(self, bits):
		self.bits = bits
		self.parent = self
		self.size = 1

	def __repr__(self):
		return 'Node(%s)'%(self.bits)

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

def readEdges():
	nodes = []
	with open(FILE, 'r') as f:
		lvs = map(int, f.readline().split())
		nodesCnt = lvs[0]
		bitsCnt = lvs[1]
		for l in f.readlines():
			lvs = map(int, l.split())
			if len(lvs) != bitsCnt:
				raise Exception('Wrong number of bits')
			bits = tuple(lvs)
			nodes.append(Node(bits))
	return (nodesCnt, nodes)

def adges(nodes):
	for a in nodes:
		for b in nodes:
			if a is not b:
				yield (a, b)

def distance(a, b):
	d = 0
	for i in xrange(0, len(a.bits)):
		if a.bits[i] != b.bits[i]:
			d+=1
	return d

if __name__ == '__main__':
	(numNodes, nodes) = readEdges()
	print(len(nodes))
	l = sum( (1 for x in adges(nodes) if distance(x[0], x[1])==1) )
	print(l)
