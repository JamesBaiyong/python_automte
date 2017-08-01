#coding=utf-8
#备份文件夹为zip

import zipfile,os

def backeup2zip(dir):

	absdir = os.path.abspath(dir)

	number = 1
	while True:
		zipFilename = os.path.basename(absdir)+'_'+str(number)+'.zip'
		if not os.path.exists(zipFilename):
			break
		number = number + 1

	print 'Creating %sd....'%(zipFilename)
	backupzip = zipfile.ZipFile(zipFilename,'w')

	for foldername,subfolders,filenames in os.walk(dir):
		print foldername,subfolders,filenames
		backupzip.write(foldername)

		#写入文件到ZIP文件
		for filename in filenames:
			#把每个文件添加到ZIP文件，以前添加的备份文件除外
			if filename.startswith(os.path.basename(absdir)+'_') and filename.endswith('.zip'):
				continue
			print 'Adding %s in %s:'%(filename,zipFilename)
			backupzip.write(os.path.join(foldername,filename))
	backupzip.close()
	print 'Done.'

backeup2zip(r".\test")