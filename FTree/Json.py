import System
import clr
clr.AddReference('System.Web.Extensions')
from System.Web.Script.Serialization import JavaScriptSerializer

#System.Diagnostics.Debug.WriteLine(s)

def LoadJson(path):
	f = open(path, 'r')
	buffer = f.read()
	f.close()
	
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

	f = open(path, 'w')
	f.write(buffer)
	f.close()

