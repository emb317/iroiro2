
import re

def CorrectPath(path):
	path = path.strip()
	path = path.replace('\\', '/')
	path = re.sub('/+$', '', path)
	if len(path) >= 2 and path[1]==':':
		path = path[0].upper() + path[1:]
	return path
