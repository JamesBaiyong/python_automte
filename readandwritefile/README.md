### 使用到的模块以及方法用法（部分扩展，部分省略）

### 1.目录导航

**文件[findword.py](./findword.py)**：查找指定文件夹内的所有的txt文件，找出指定单词，并统计出现次数

**文件[madlib.py](./madlib.py)**:将正则表达式匹配的单词修改为用户输入的单词

**文件[randomQuizGeneratir.py](./randomQuizGeneratir.py)**:创建35份50个美国州的首府问答卷，且每一份问答题是随机的

**文件夹[Quize&Answer](./Quize&Answer)**:存放randomQuizGeneratir.py创建的问答试卷的文件夹

**文件[test.txt](./test.txt)**:用于测试madlib.py

### 2.OS

```python
import os
```



**os.listdir(path)**： 列出指定文件夹下的文件

**os.makers(filename)**：创建文件夹,会穿件中间文件夹，保证完整路径名

**os.path.abspath(path)**：返回参数的绝对路径

**os.path.relpath(path,start)**返回从start路径到path的相对路径

**os.path.isbas(path)**：判断是否是绝对路径

**os.path.getsize(path)**：返回path参数中文件的字节数

**os.path.exists(path)**：判断路径是否存在

**os.chdir(path)**：改变路径到指定路径

**os.system(cmd)**：执行命令

**os.startfile(file)**：打开文件



### 3.random

```py
import random
```



**random.randint(a,b)**:随机生成a<= n <=b范围内的整数

**random.sample('abcdefg',3)**:随机生成3个指定范围内的字符

**random.choice(['a','b','c','d'])**:随机选取指定列表的一个值

**random.shuffle(items)**:随机排列列表中的元素，打乱原本的顺序



