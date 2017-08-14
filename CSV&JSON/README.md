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

