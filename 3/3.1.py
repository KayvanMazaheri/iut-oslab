import os, sys, stat
import argparse


def createFile(permission, path):
	# print int(permission, 8)
	# print path
	file = os.open(path, os.O_CREAT, int(permission, 8))
	os.close(file)
	return

def writeToPath(path):
	s = raw_input()
	file = os.open(path, os.O_RDWR | os.O_CREAT, 00755)
	os.write(file, s)
	os.close(file)
	return

def catFile(path):
	file = os.open(path, os.O_RDONLY)
	print os.read(file, 200000)
	os.close(file)

parser = argparse.ArgumentParser()
parser.add_argument("-c", nargs=2)
parser.add_argument("-w")
parser.add_argument("-r")
args = parser.parse_args()

# print args
if args.c:
	createFile(args.c[0], args.c[1])
elif args.w:
	writeToPath(args.w)
elif args.r:
	catFile(args.r)
else:
	print "wrong!"