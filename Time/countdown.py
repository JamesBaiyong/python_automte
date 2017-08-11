#coding=utf-8


import time, subprocess

timeLeft = 10
while timeLeft > 0:
    print '%s seconds play alarm.wav' %timeLeft
    time.sleep(1)
    timeLeft = timeLeft - 1

#
subprocess.Popen(['start','alarm.wav'], shell=True)