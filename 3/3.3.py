import os, sys, stat
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-matrix", nargs=3)
parser.add_argument("-vector", nargs=2)
parser.add_argument("-readMat", nargs='*')

args = parser.parse_args()

def catFile(path):
	file = os.open(path, os.O_RDONLY)
	print os.read(file, 200000)
	os.close(file)

if args.matrix:
	m, n, path = int(args.matrix[0]), int(args.matrix[1]), args.matrix[2]
	file = os.open(path, os.O_RDWR | os.O_CREAT, 00755)
	for i in range(m):
		s = raw_input()
		os.write(file, s+"\n")
	os.close(file)
elif args.vector:
	m, path = int(args.vector[0]), args.vector[1]
	file = os.open(path, os.O_RDWR | os.O_CREAT, 00755)
	s = raw_input()
	os.write(file, s+"\n")
	os.close(file)
elif args.readMat:
	if len(args.readMat) == 1:
		catFile(args.readMat[0])
	else:
		m, n, path = int(args.readMat[0]), int(args.readMat[1]), args.readMat[2]
		file = os.open(path, os.O_RDONLY)
		text = os.read(file, 200000)
		os.close(file)
		text = text.split('\n')
		line = text[m].split(' ')
		print line[n]


