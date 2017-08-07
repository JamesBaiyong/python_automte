#coding=utf-8
#使用字典暴力破解加密的PDF文件

import PyPDF2
#加载PDF文件
pdfFile = open('encryptTest.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)

#尝试每一条密码
with open('dictionary.txt') as f:
	print 'decrypting.....'
	for line in f:
		password=line.strip().lower()
		if pdfReader.decrypt(password):
			print 'The password is:' + password
			break
print 'OVER....'