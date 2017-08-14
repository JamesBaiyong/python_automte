#coding=utf-8
#调用发送短信模块，发送实时天气预报

import json,requests
from sendMessage import textmyself

#请求天气预报JSON格式
url ='https://free-api.heweather.com/v5/now?city=%s&key=%s' % ('yourcity','yourKEY')
response = requests.get(url)
response.raise_for_status()

#将数据转为python格式
weatherDate = json.loads(response.text,encoding='utf-8')
w = weatherDate["HeWeather5"]
now_time=w[0]['basic']['update']['loc']
now_cod=w[0]['now']['cond']['txt']
now_tmp=w[0]['now']['tmp']
now_fl=w[0]['now']['fl']
messages =  u'\n现在是:%s\n天气是：%s\n温度:%s摄氏度\n体感温度是:%s摄氏度'\
            %(now_time,now_cod,now_tmp,now_fl)

textmyself(messages)
