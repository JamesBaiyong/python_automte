#coding=utf-8
#使用正则表达式确保口令是强口令

import re

def StongPass(str):
	if len(str)<8:
		return False
	numberRe=re.compile(r'[0-9]')
	lowerRe=re.compile(r'[a-z]')
	upper=re.compile(r'[A-Z]')
	symbol=re.compile(r'[._!@#$%^&*()_+]+')

	if numberRe.search(str) and lowerRe.search(str)\
			and upper.search(str) and symbol.search(str):
		return  True
	else:
		return False

passwod = raw_input('Enter Stong Password')
#一直循环，直到输出强口令
while True:
	if StongPass(passwod):
		print 'This is a stong password^.^'
		break
	else:
		print 'That\'s not a stong password-.-'
		passwod = raw_input('Enter Stong Password')