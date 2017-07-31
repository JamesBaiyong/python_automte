#coding=utf-8
#查找指定文件夹内的所有的txt文件，找出指定单词，并统计出现次数

import os,re

def getFile(director):
	txts = []
	txtrege=re.compile( r'\.txt$')
	for filename in os.listdir(director):
		mo = txtrege.search(filename)
		if mo:
			txts.append(filename)
	return txts

def findWord(str,director):
	txts = getFile(director)
	print txts
	count=0
	query = re.compile(str)
	for txt in txts:
		dirfile = director+'\\'+txt
		with open(dirfile) as f:
			for i in f :
				mo = query.search(i)
				if mo:
					count+=1
					print 'file %s have key word and in line:%s'%(txt,i)
	print 'key word appear %s times'%count


findWord('Helena',r'.\Quize&Answer')

