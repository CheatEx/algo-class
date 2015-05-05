#!/usr/bin/env python

import sys

def readProblem(fileName):
	items = {}
	with open(fileName, 'r') as f:
		h = map(int, f.readline().split())
		vertCnt = h[0]
		edgeCnt = h[1]
		for l in f.readlines():
			il = map(int, l.split())
			items[(il[0], il[1])] = (il[0], il[1], il[2])
	return (vertCnt, edgeCnt, items)

def calc(vertCnt, edges):
	src = [[0]*vertCnt for i in xrange(0, vertCnt)]
	dst = [[0]*vertCnt for i in xrange(0, vertCnt)]
	#print('0d=%s, 1d=%s'%(len(src), len(src[0])))
	for i in xrange(vertCnt):
		for j in xrange(vertCnt):
			if (i == j):
				src[i][j] = 0
			elif (i+1, j+1) in edges:
				src[i][j] = edges[(i+1, j+1)][2]
			else:
				src[i][j] = sys.maxint
	
	for k in xrange(1, vertCnt+1): # 0..vertCnt
		for i in xrange(vertCnt):
			for j in xrange(vertCnt):
				v = min(
					src[i][j],
					src[i][k-1]+src[k-1][j])
				if i == j and v < 0:
					raise Exception("Negative loop i=%s, j=%s, k=%s, v=%s"%(i, j, k, v))
				dst[i][j] = v
		if k % 10 == 0:
			print('%s done...'%(k))
		src, dst = dst, src

	m = sys.maxint
	for i in xrange(vertCnt):
		for j in xrange(vertCnt):
			if src[i][j] < m:
				m = src[i][j]
	return m

if __name__ == '__main__':
	for file in ('g1.txt', 'g2.txt', 'g3.txt'):
		try:
			(vertCnt, edgeCnt, edges) = readProblem(file)
			m = calc(vertCnt, edges)
			print('Result for file %s is %s'%(file, m))
		except Exception, e:
			print('Excetion on file %s, message: %s'%(file, e.message))
