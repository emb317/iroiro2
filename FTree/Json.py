import System
from System.IO import *
from System.Text import *

import clr
clr.AddReference('System.Web.Extensions')
from System.Web.Script.Serialization import JavaScriptSerializer


#System.Diagnostics.Debug.WriteLine(s)

def LoadJson(path):
	sr = StreamReader(path, Encoding.GetEncoding("UTF-8"));
	buffer = sr.ReadToEnd();
	sr.Close();
	return JavaScriptSerializer().DeserializeObject(buffer)
	
def SaveJson(path, config):
	tmp = JavaScriptSerializer().Serialize(config)
	buffer = ""
	
	inStr = False
	for s in tmp:
		if s == '"':
			inStr = not inStr
		
		if not inStr:
			if s == ',':
				s = s + '\n'
			if s == '{' or s == '[':
				s = s + '\n'
			if s == '}' or s == ']':
				s = '\n' + s
		buffer += s
		
	tmp = buffer
	buffer = ""
	indent = 0
	for s in tmp.split('\n'):
		if len(s) > 0 and (s[0] == '}' or s[0] == ']'):
			indent -= 1

		buffer += '  ' * indent + s + '\n'

		if len(s) > 0 and (s[-1] == '{' or s[-1] == '['):
			indent += 1

	sw = StreamWriter(path, False, Encoding.GetEncoding("UTF-8"));
	sw.Write(buffer);
	sw.Close();
