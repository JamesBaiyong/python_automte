### 1.目录导航

**[quickWeather.py](./quickWeather.py)**:使用返回JSON格式的API查询天气状况

**[removeCsvHeader.py](./removeCsvHeader.py)**:批量删除CSV文件第一行，另存为新文件



### 2.CSV模块

CSV表示“Comma-Separated Values(逗号分隔的值)”，是简化的电子表格，保存为纯文本文件。

```py
import csv
```

#### Reader对象

Reader对象可用遍历CSV文件中的每一行。

使用：

```she
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
```

exampleData[0]\[0]:表示进入第一个列表，并给出第一个字符串。

#### Writer对象

Writer对象将数据写入CSV文件。

```python
import csv
```

使用：

```shell
outputFile = open('output.csv','w',newline='')
outputWriter = csv.writer(outputFile)
outputWrite.writerow(['spam','eggs','ham','bacon'])
```

Write对象的writerow方法接收一个列表参数。



### 3.JSON模块

Python的JSON模块处理了JSON数据字符串和python值之间转换的所有细节，主要用到json.loads()和json.dumps()函数。

使用loads()函数读取JSON：

```shell
>>> import json
>>> stringOfJsonData='{"name":"Jake","isCat":true,"miceCaught":0,"felineIQ":null}'
>>> jsonDataAsPythonValue = json.loads(stringOfJsonData)
>>> jsonDataAsPythonValue
{u'miceCaught': 0, u'isCat': True, u'felineIQ': None, u'name': u'Jake'}
>>>
```

向loads()函数传入一个JSON数据字符串，函数会将该数据返回为一个python字典。python字典是无序的，所以键值对以不同的顺序出现。

使用dumps()函数写出JSONl：

```shell
>>> import json
>>> pythonValue = {'isCat':True,'miceCaught':0,'name':'Zophie','felineIQ':None}
>>> stringOfJsonData = json.dumps(pythonValue)
>>> stringOfJsonData
'{"miceCaught": 0, "isCat": true, "felineIQ": null, "name": "Zophie"}'
>>>
```

dumps()函数将传入的python值转换成JSON格式的数据字符串。







