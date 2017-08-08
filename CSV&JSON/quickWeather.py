#coding=utf-8
#使用返回JSON格式的API查询天气状况

import json,sys,requests

if len(sys.argv)<2:
	print 'Usage: quickWeather.py [Location]'
	sys.exit()
	#将命令行参数出第一个外保存到变量中
location = ' '.join(sys.argv[1:])

#使用和风天气提供的API，查询三天的天气状况
url ='https://free-api.heweather.com/v5/forecast?city=%s&key=%s' % (location,'yourkey')
response = requests.get(url)
response.raise_for_status()

#将数据转为python格式
weatherDate = json.loads(response.text,encoding='utf-8')
w = weatherDate["HeWeather5"]


print '='*40
print  u'明天是:%s'%w[0]['daily_forecast'][0]['date']
print u'白天天气是:%s'%w[0]['daily_forecast'][0]['cond']['txt_d']
print u'全天最高温度:%s摄氏度，最低温度:%s摄氏度'%(w[0]['daily_forecast'][0]['tmp']['max'],w[0]['daily_forecast'][0]['tmp']['min'])
print '='*40

print '='*40
print  u'明天是:%s'%w[0]['daily_forecast'][1]['date']
print u'白天天气是:%s'%w[0]['daily_forecast'][1]['cond']['txt_d']
print u'全天最高温度:%s摄氏度，最低温度:%s摄氏度'%(w[0]['daily_forecast'][1]['tmp']['max'],w[0]['daily_forecast'][1]['tmp']['min'])
print '='*40

print '='*40
print  u'后天是:%s'%w[0]['daily_forecast'][2]['date']
print u'白天天气是:%s'%w[0]['daily_forecast'][2]['cond']['txt_d']
print u'全天最高温度:%s摄氏度，最低温度:%s摄氏度'%(w[0]['daily_forecast'][2]['tmp']['max'],w[0]['daily_forecast'][2]['tmp']['min'])
print '='*40
