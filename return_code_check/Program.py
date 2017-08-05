# coding: utf-8

import sys
from System import *
from System.IO import *
import re

max_cnt = 0
max_byte = 500 * 1024
name_filter = []
sub_dir = False
print_condition = "True"

def PrintFile(path):
	fs = open(path, 'rb', max_byte)
	
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
	
	
	if eval(print_condition, {'CR':cr_cnt, 'LF':lf_cnt, 'CRLF':crlf_cnt, 'cr':cr_cnt, 'lf':lf_cnt, 'crlf':crlf_cnt}):
		print('{:>5} : {:>5} : {:>5} : {}'.format(crlf_cnt, lf_cnt, cr_cnt, path))

def CheckDir(path):
	if sub_dir:
		try:
			for dir_path in Directory.GetDirectories(path):
				CheckDir(dir_path)
		except:
			print(sys.exc_info)

	try:
		for file_path in Directory.GetFiles(path):
			file_path = Path.GetFullPath(file_path)
			if len(name_filter):
				file_name = Path.GetFileName(file_path)
				for f in name_filter:
					if re.search(f, file_name):
						PrintFile(file_path)
						break
			else:
				PrintFile(file_path)
	except:
		print(sys.exc_info())

def PrintHelp():
	print('[ヘルプ]')
	print(' '+Path.GetFileNameWithoutExtension(sys.argv[0]) + '[options] [path1 path2 path3 ...]')
	print(' [options]')
	print('  -F フィルタ : フィルタで指定したファイル名のファイルを検索対象とする。')
	print('              : 正規表現でマッチングを行うため -F "Test .*\.txt" のような記述が可能。')
	print('  -N 検出数   : CR または LF の検出数が指定した数に達したらそのファイルの検出を終了する。')
	print('  -B バイト数 : ファイルの最大読み込みサイズ。')
	print('  -H / -help  : このヘルプを表示する。')
	print('  -R          : サブディレクトリも対象とする。')
	print('  -C          : 表示条件式を指定する。CR,LF,CRLF にカウント数が入っているため条件に使用する。')
	print('              : 例 -C "(CR > 0 or LF > 0 ) and CRLF == 0" ')
	print('              :    この例ではCRまたはLFが0でなく、CRLFが見つからない場合のみ表示される。')
	print(' [path1 path2 path3 ...]')
	print('  検出対象があるパスを指定する。指定しない場合カレントディレクトリが対象となる。')
	sys.exit()

opt = ''
path_list = []
for i in sys.argv[1:]:
	if i[0]=='-':
		if i.find('help') >= 0:
			PrintHelp()
		elif len(i) != 2:
			print('Error:Invalid option : ' + i)
			PrintHelp()
		elif i[1].upper()=='F':
			opt = 'F'
		elif i[1].upper()=='N':
			opt = 'N'
		elif i[1].upper()=='B':
			opt = 'B'
		elif i[1].upper()=='R':
			sub_dir = True
		elif i[1].upper()=='H':
			opt = 'H'
			PrintHelp()
		elif i[1].upper()=='C':
			opt = 'C'
		else:
			print('Error:Unknow option : ' + i)
			PrintHelp()
	else:
		if opt=='F':
			name_filter.append(i)
		elif opt=='N':
			max_cnt = int(i)
		elif opt=='B':
			max_byte = int(i)
		elif opt=='C':
			print_condition = i
		else:
			path_list.append(i)
			
		opt = ''

print('{:>5} : {:>5} : {:>5} : Path'.format('CRLF','LF','CR'))
if len(path_list)==0:
	CheckDir('.\\')
else:
	for i in path_list:
		CheckDir(i)
