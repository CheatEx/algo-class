#!/usr/bin/env python

import sys

FILE = 'jobs.txt'

class Job(object):
	def __init__(self, weight, length):
		super(Job, self).__init__()
		self.weight = weight
		self.length = length

	def __repr__(self):
		return "[w=%s, l=%s]"%(self.weight, self.length)

def readJobs():
	jobs = list()
	with open(FILE, 'r') as f:
		num = f.readline()
		for l in f.readlines():
			split = l.split()
			jobs.append(Job(int(split[0]), int(split[1])))
	return jobs

def weighedSum(jobs):
	res = 0
	t = 0
	for j in jobs:
		t += j.length
		res += t*j.weight
	return res

def diffCmp(j1, j2):
	j1d = j1.weight - j1.length
	j2d = j2.weight - j2.length
	if j1d<j2d:
		return -1
	elif j1d>j2d:
		return 1
	else:
		if j1.weight < j2.weight:
			return -1
		elif j1.weight > j2.weight:
			return 1
		else:
			return 0


if __name__ == '__main__':
	jobs = readJobs()
	byDiff = sorted(jobs, reverse = True,
		cmp = diffCmp)
	print(weighedSum(byDiff))
	byRatio = sorted(jobs, reverse=True,
		key = lambda j: j.weight / j.length)
	print(weighedSum(byRatio))
