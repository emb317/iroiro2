
import re
from System.Text import *

def CorrectPath(path):
	path = path.strip()
	path = path.replace('\\', '/')
	path = re.sub('/+$', '', path)
	if len(path) >= 2 and path[1]==':':
		path = path[0].upper() + path[1:]
	return path

# https://ameblo.jp/only-human/entry-10104676221.html
def ConvertEncoding(src, srcEnc, destEnc):
	src_temp = Encoding.ASCII.GetBytes(src)
	dest_temp = Encoding.Convert(srcEnc, destEnc, src_temp)
	return destEnc.GetString(dest_temp)

def ConvertEncoding_ShiftJisToUtf8(src):
	return ConvertEncoding(src, Encoding.GetEncoding("Shift_JIS"), Encoding.UTF8)

def ConvertEncoding_Utf8ToShiftJis(src):
	return ConvertEncoding(src, Encoding.UTF8, Encoding.GetEncoding("Shift_JIS"))