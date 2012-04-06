#!/usr/bin/env python

FILE = 'kargerAdj.txt'
ROUNDS = 100

def minCut(graph):
	return 1

def readGraph():
	graph = []
	with open(FILE, 'r') as f:
		for l in f.readlines():
			nodeLine = map(int, l.split())
			graph.insert(nodeLine[0], nodeLine[1:])
	return graph

def copy(graph):
	new = []
	for v in graph:
		new.append(list(v))
	return new


if __name__ == '__main__':
	g = readGraph()
	r = (minCut(copy(g)) for i in range(0, ROUNDS))
	print min(r)
