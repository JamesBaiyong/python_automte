#coding=utf-8
#合并指定文件夹中的PDF

import os,PyPDF2

pdffile=[]
for filename in os.listdir('./Pdffile'):
	if filename.endswith('.pdf'):
		pdffile.append(filename)
pdffile.sort(key=str.lower)
pdfwrite = PyPDF2.PdfFileWriter()

#读取每个PDF文档
for filename in pdffile:
	print filename
	filename1='./Pdffile/'+filename
	pdffileobj = open(filename1,'rb')
	pdfreader = PyPDF2.PdfFileReader(pdffileobj)
	for pagenum in range(pdfreader.numPages):
		pageobj = pdfreader.getPage(pagenum)
		pdfwrite.addPage(pageobj)

pdfoutput = open('allminutes.pdf','wb')
pdfwrite.write(pdfoutput)
pdfoutput.close()

