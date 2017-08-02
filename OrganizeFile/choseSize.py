#coding=utf-8
#查找指定文件夹下指定大写的文件

import os

def search(path,size):
	for foldername, subfolders, filenames in os.walk(path):
		for filename in filenames:
			filenamesize=os.path.join(foldername,filename)
			get_size=os.path.getsize(filenamesize)
			if get_size>size:
				print "File:%s is %s KB"%(filenamesize,get_size)

search('G:\\work',1024*1024)