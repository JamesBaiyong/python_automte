#coding=utf-8
#用正则表达式实现函数strip()功能

import re

def stripDef(str):
	strip=re.compile(r'^\s+(.*)\s+$')  #匹配开头和结尾都有空格，中间有字符的字符串
	mo=strip.search(str)
	return mo.group(1)   #返回括号中的内容，就是去掉前后空格的内容

strtext = '   Hello World!   '
print stripDef(strtext)
