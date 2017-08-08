#coding=utf-8
#批量删除CSV文件第一行，另存为新文件

import os,csv

for csvfilename in os.listdir('./CSVfile'):
	if not csvfilename.endswith('.csv'):
		continue

	print('Removing header from ' + csvfilename + '...')
	#读取CSV源文件
	csvRow = []
	csvFile = open('./CSVfile/'+csvfilename)
	readerObj = csv.reader(csvFile)
	for row in readerObj:
		if readerObj.line_num == 1:
			continue
		csvRow.append(row)
	csvFile.close()

	csvFileWrite = open(os.path.join('./CSVdone',csvfilename),'w')
	#写入新的CSV文件
	csvWriter = csv.writer(csvFileWrite)
	for row in csvRow:
		csvWriter.writerow(row)
	csvFileWrite.close()
