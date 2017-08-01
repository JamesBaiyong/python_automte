#coding=utf-8
#将有美式风格日期的文件名更改为中式风格日期的文件名，该正则表达式不能完全正确的匹配合法日期

import  re,os,shutil


datePattern = re.compile(r"""^(.*?) # 匹配日期前的文本
    ((0|1)?\d)- # 一位或则两位月份
    ((0|1|2|3)?\d)- # 一位或则两位日期
    ((19|20)\d\d) # 4位年份从19到20之间
    (.*?)$ # 匹配所有日期后的文本
    """, re.VERBOSE)

for filename in os.listdir(r'.\test'):
	mo = datePattern.search(filename)
	if mo is None:
		continue
	print  mo.group()
	beforPart = mo.group(1)
	dayPart = mo.group(4)
	monthPart = mo.group(2)
	yearPart = mo.group(6)
	afterPart = mo.group(8)

	chinafilename =beforPart+yearPart+'-'+monthPart+'-'+dayPart+afterPart

	#获取完整的文件路径
	absWorkingDir = os.path.abspath(r'.\test')
	filename = os.path.join(absWorkingDir,filename)
	chinafilename = os.path.join(absWorkingDir,chinafilename)

	print 'Renaming "%s" to "%s"...'%(filename,chinafilename)
	shutil.move(filename,chinafilename)

