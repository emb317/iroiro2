# coding: utf-8

import sys
from System import *
from System.IO import *

def PrintFile(path):
	fs = FileStream(path, FileMode.Open, FileAccess.Read)
	
	crlf_cnt = 0
	
	for i in range(max(fs.Length-2, 500)):
		if fs.ReadByte()==13:
			if fs.ReadByte()==10:
				crlf_cnt += 1
				if crlf_cnt >= 10:
					break
	
	# 閉じる
	fs.Close()
	
	if crlf_cnt==0:
		print(str(crlf_cnt) + " : " + path)

def CheckDir(path):
	try:
		for dir_path in Directory.GetDirectories(path):
			CheckDir(dir_path)
	except:
		pass

	try:
		for file_path in Directory.GetFiles(path):
			PrintFile(file_path)
	except:
		pass

for i in range(1, len(sys.argv)):
	CheckDir(sys.argv[i])
