# coding: utf-8

import sys
from System import *
from System.IO import *

max_cnt = 0
max_byte = 0
name_filter = []

def PrintFile(path):
	fs = open(path, "rb")
	
	crlf_cnt = 0
	lf_cnt = 0
	cr_cnt = 0
	
	cnt = 0
	cr = False
	for c in fs.read():
		if ord(c)==10:
			lf_cnt += 1
			if cr:
				crlf_cnt += 1

		if max_cnt > 0 and (cr_cnt >= max_cnt or lf_cnt >= max_cnt):
			break

		if ord(c)==13:
			cr = True
			cr_cnt += 1
		else:
			cr = False

		cnt += 1
		if max_byte > 0 and cnt >= 200:
			break

	fs.close()
	
	#if crlf_cnt==0:
	print("{:>5} : {:>5} : {:>5} : {}".format(crlf_cnt, lf_cnt, cr_cnt, path))

def CheckDir(path):
	try:
		for dir_path in Directory.GetDirectories(path):
			CheckDir(dir_path)
	except:
		print(sys.exc_info)

	try:
		for file_path in Directory.GetFiles(path):
			if len(name_filter):
				for f in name_filter:
					if file_path.find(f) >= 0:
						PrintFile(file_path)
						break
			else:
				PrintFile(file_path)
	except:
		print(sys.exc_info())

name_filter = ["Swc"]
max_cnt = 5
print("{:>5} : {:>5} : {:>5} : Path".format("CRLF","LF","CR"))
for i in range(1, len(sys.argv)):
	CheckDir(sys.argv[i])
