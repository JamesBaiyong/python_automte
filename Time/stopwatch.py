#coding=utf-8
#超级秒表，记录每一圈用时和总共用时

import time

raw_input('Press ENTER to begin.Afterwards,press ENTER to "click" the stopwatch.')
print 'Started'
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
	while True:
		raw_input('Press to take notes last lapTime')#按下ENTER键后记录上一圈用时
		lapTime = round(time.time() - lastTime,2)#一圈的用时
		totalTime = round(time.time() - startTime,2)#总共用时
		print 'Lap #%s:%s (%s)' % (lapNum,totalTime,lapTime)
		lapNum +=1 #增加一圈
		lastTime = time.time()
except KeyboardInterrupt:
	print '\nDone.'
