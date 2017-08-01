#coding=utf-8
#选择一个文件类型，复制到指定路径

import os,shutil

def copy(file,dirpath,dir):
	#判断指定路径是否存在，没有则新建
	if not os.path.exists(dir):
		os.mkdir(dir)

	try:
		for foldername, subfolders, filenames in os.walk(dirpath):
			print filenames,subfolders,foldername
			#查找指定文件，并且复制
			for filename in filenames:
				if filename.endswith('.'+file):
					print os.path.join(foldername,filename)
					shutil.copy(os.path.join(foldername,filename),dir)


	except shutil.Error as e:
		print 'something error:%s but Finished copying file'%e

copy('jpg','.','test\\jpg')