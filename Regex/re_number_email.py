#coding=utf-8
#从粘贴板中找到电话号码和邮箱，并把电话号码和邮箱复制会粘贴板

import re,pyperclip

matches=[]

#creat number regex
numberRegex = re.compile(r'''(
	(\d{3}|(\d{3}))?  
	(\s|-|\.)?
	(\d{3})
	(\s|-|\.)
	(\d{4})
)''',re.VERBOSE)

#create email regex
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+
	@
	[a-zA-Z0-9.-]+
	(\.[a-zA-Z]{2,4})
)''',re.VERBOSE)

text = str(pyperclip.paste())

#匹配电话号码后整理格式加入到列表
for groups in numberRegex.findall(text):
	phonenumber = '-'.join([groups[1],groups[4],groups[6]])
	# print groups[0]
	matches.append(phonenumber)

#将匹配的邮箱地址加入到列表
for groups in emailRegex.findall(text):
	matches.append(groups[0])

if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print 'Now coping to clipboard'
	print '\n'.join(matches)
else:
	print 'NO numebr and email address found.'


