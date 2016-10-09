import os, sys, stat
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-make", nargs=5)

args = parser.parse_args().make

dirPath = args[0]
prefix = args[1]
ext = args[2]
v1, v2 = int(args[3]), int(args[4])

if not os.path.isdir(dirPath):
	os.mkdir(dirPath, 0755)

for x in xrange(v1,v2+1):
	file = os.open(dirPath+prefix+"_"+str(x)+"."+ext, os.O_CREAT)
	os.close(file)