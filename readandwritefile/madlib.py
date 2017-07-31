#coding=utf-8
#将正则表达式匹配的单词修改为用户输入的单词

import re

wordrege = re.compile('[A-Z]{2,}') #匹配两个极其以上的大写字母单词
with open('./text.txt','r') as f:
	txt = f.read()

while True:
	mo = wordrege.search(txt)
	if mo is None:
		print 'No words need replaced.'
		break
	word = raw_input('Enter a '+ mo.group().lower()+':\n')
	txt = wordrege.sub(word,txt,count=1)
	with open('./text.txt','w') as f:
		f.write(txt)
print txt