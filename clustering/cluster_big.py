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
		return repr(self.bits)

	def __hash__(self):
		return hash(self.bits)

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

def readNodes():
	nodes = {}
	with open(FILE, 'r') as f:
		lvs = map(int, f.readline().split())
		nodesCnt = lvs[0]
		bitsCnt = lvs[1]
		for l in f.readlines():
			lvs = l.split()
			if len(lvs) != bitsCnt:
				raise Exception('Wrong number of bits')
			bits = tuple([s=='1' for s in lvs])
			node = Node(bits)
			nodes[bits]=node
	return (nodesCnt, nodes)

def gen(bits, dist):
	l = len(bits)
	if dist==1:
		for i in xrange(0, l):
			yield bits[:i]+(not bits[i],)+bits[i+1:]
	elif dist==2:
		for i in xrange(0, l):
			for j in xrange(i+1, l):
				yield bits[:i]+(not bits[i],)+bits[i+1:j]+(not bits[j],)+bits[j+1:]
	else:
		raise Exception()

def merge(nodes, dist):
	for n in nodes.itervalues():
		for cb in gen(n.bits, dist):
			if cb in nodes:
				union(n, nodes[cb])

if __name__ == '__main__':
	(cnt, nodes) = readNodes()
	# c = 0
	# for b in nodes.itervalues():
	# 	c+=1
	# 	print(">>> "+str(b))
	# 	for g in gen(b.bits, 1):
	# 		print(g)
	# 	if c == 10:
	# 		break;

	merge(nodes, 1)
	merge(nodes, 2)
	
	tmp = set()
	for n in nodes.itervalues():
		tmp.add(find(n))
	print(len(tmp))
