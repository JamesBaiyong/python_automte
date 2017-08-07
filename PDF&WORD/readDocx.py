#coding=utf-8
#只获取文本信息

import docx

def getText(filename):
	doc = docx.Document(filename)
	fulltText = []
	for para in doc.paragraphs:
		fulltText.append(para.text)
	return '\n'.join(fulltText)