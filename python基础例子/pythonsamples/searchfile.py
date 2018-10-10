# coding=utf-8
import os
def searchFile(path,filename):
	with os.scandir(path) as it:
		for entry in it:
			if entry.is_file() and filename in entry.name :
				print(entry.path.encode('utf-8'))
			elif entry.is_dir():
				searchFile(entry.path,filename)
				
searchFile('/Downloads','py')