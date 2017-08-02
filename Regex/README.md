## 正则表达式

### 1.文件导航

**文件[re_number_email.py](./re_number_email.py)**：从粘贴板中找到电话号码和邮箱，并把电话号码和邮箱复制会粘贴板

**文件[realizeStrip.py](./realizeStrip.py)**：用正则表达式实现函数strip()功能

**文件[stongPassword.py](./stongPassword.py)**：使用正则表达式确保口令是强口令



### 2.使用正则表达式步骤

SETP1.导入正则表达式模块

SETP2.用re.compile()创建一个Regex对象。

SETP3.向Regex对象使用search方法传入想查找的字符串，返回一个Match对象

SETP4.调用match的group方法的到正则表达式匹配的文本

### 3.正则表达式字符意义

| 字符                | 意义                  |
| ----------------- | :------------------ |
| .                 | 任意的一个字符             |
| alb               | 字符a或则字符b            |
| [abc]             | 字符a或则b或则c的一个字符      |
| [a-z],[A-Z],[0-9] | 所有小写字母，大写字母，所有数字    |
| \s，\S             | 空格，不是空格             |
| \w,\W             | 单词，不是单词             |
| \d，\D             | 数字，不是数字             |
| ^                 | 字符串的起始位置            |
| $                 | 字符串的结尾位置            |
| *                 | 重复>=0次              |
| +                 | 重复>=1次              |
| ？                 | 重复0或者1次             |
| {m}               | 重复m次。例如A{4}就相当与AAAA |
| {m.n}             | 重复m-n次              |

### 4.正则表达式主要函数

**compile()**:创建一个正则表达式对象

**search()**:返回一个Match对象，也就是只返回第一次匹配到的文本

**findall()**:返回一组Match对象，也就是返回被查找字符串中所有的匹配

**sub()**:需要传入两个参数，第一个参数是一个字符串，用与取代发现的匹配，第二个参数（正则表达式）。返回替换完毕成后的字符串

### 5.分组

分组是通过 "(" 和 ")" 元字符来标识的，组从0开始计算，小组是从左向右计数的，从1开始。

例子：

```pytho
In [14]: p = re.compile('(a(b)c)d')

In [15]: mo = p.search('abcd')

In [16]: mo.group()
Out[16]: 'abcd'

In [17]: mo.group(0)
Out[17]: 'abcd'

In [18]: mo.group(1)
Out[18]: 'abc'

In [19]: mo.group(2)
Out[19]: 'b'
```



### 6.贪心和非贪心匹配

0python正则表达式默认是“贪心”匹配，这表示尽可能多的匹配文本，比如文本有两段匹配字符，那么贪心匹配则会匹配所有文本，但是非贪心匹配则是匹配第一段字符。使用非贪心匹配需要在匹配文本条件外加上“？”。

看例子：

```py
In [28]: greedyHaRegex = re.compile(r'(ha){3,5}')

In [29]: mo1=greedyHaRegex.search('hahahahaha')

In [30]: mo1.group()
Out[30]: 'hahahahaha'

In [33]: nongreedyHaRegex = re.compile(r'(ha){3,5}?')

In [34]: mo2=nongreedyHaRegex.search('hahahahaha')

In [36]: mo2.group()
Out[36]: 'hahaha'
```



