#!/usr/bin/env python

import sys

FILE = 'SCC.txt'

sys.setrecursionlimit(100000)

def invert(graph):
	inversion = {}
	for k in graph.iterkeys():
		inversion[k] = []
	for node, edges in graph.iteritems():
		for edge in edges:
			if edge not in inversion:
				inversion[edge] = []
			inversion[edge].append(node)
	return inversion

def calcOrder(graph):
	order = []
	explored = set()
	for i in xrange(1, len(graph)+1):
		if i not in explored:
			dfsOrder(graph, i, explored, order)
	return order

def dfsOrder(graph, node, explored, order):
	explored.add(node)
	for i in graph[node]:
		if i not in explored:
			dfsOrder(graph, i, explored, order)
	order.append(node)

def scc(graph, order):
	sccs = {}
	explored = set()
	order.reverse()
	for i in order:
		if i not in explored:
			leaded = []
			dfsScc(graph, i, explored, leaded)
			sccs[i] = leaded
	return sccs

def dfsScc(graph, node, explored, leaded):
	explored.add(node)
	leaded.append(node)
	if node in graph:
		for i in graph[node]:
			if i not in explored:
				dfsScc(graph, i, explored, leaded)

def readGraph():
	graph = {}
	with open(FILE, 'r') as f:
		for l in f.readlines():
			nodeLine = map(int, l.split())
			node = nodeLine[0]
			edge = nodeLine[1]
			if node not in graph:
				graph[node]=[]
			graph[node].append(edge)
	return graph

if __name__ == '__main__':
	graph = readGraph()
	#print graph
	inversion = invert(graph)
	#print inversion
	order = calcOrder(inversion)
	#print order
	components = scc(graph, order)
	lengths = list( map(lambda l: len(l), components.itervalues()) )
	lengths.sort()
	lengths.reverse()
	print lengths
	#print components