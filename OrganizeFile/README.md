

### 1.目录导航

**文件[backe2zip.py](./backe2.zip.py)**:备份文件夹为zip

**文件[choseCopy.py](./choseCopy.py)**:选择一个文件类型，复制到指定路径

**文件[renameDates.py](./renameDates.py)**:将有美式风格日期的文件名更改为中式风格日期的文件名，该正则表达式不能完全正确的匹配合法日期

**文件[choseSize.py](./choseSize.py)**:查找指定文件夹下指定大写的文件



### 2.shutil模块：

```python
import shutil
```

用于在python程序中复制，移动，改名以及删除文件

**shutil.copy(srcpath,despath)**:将路径srcpath的文件复制到路径despath处的文件夹

**shutil.copytree(srcpath,despath)**:将路径srcpath的整个文件夹包括子文件夹复制到路径despath处的文件夹

**shutil.move(srcpath,despath)**:将路径srcpath的文件移动到路径despath处的文件夹



### 3.OS模块

```python
import os
```

**os.unlink(path)**:删除path处的文件

**os.rmtree(path)**:删除path处的文件夹极其包含的所有文件和文件夹

**os.walk(path)**:便利目录，通常在for循环中使用，返回三个值，分别是：

（1）.当前文件夹名称的字符串

（2）.当前文件夹中子文件的字符串的列表

（3）.当前文件夹中文件的字符串列表



### 4.zipfile模块

```python
import zipfile
zipfilename=zipfile.ZipFile('example.zip')
```

创建一个zip文件时，需要调用zipfile.ZipFile()函数，向它传入一个字符串

**zipfilename.namelist()**：列出zip文件中的文件夹极其文件

**zipfilename.getinfo()**：可以获取zip文件的信息，使用file_size和compress_size可分别获取压原本文件大写和压缩后的大小

**zipfilename.extract()***:解压zip文件

**zipfilename.write('test.txt',compress_type=zipfile.ZIP_DEFLATED)**创建和添加到zip文件,compress_type指定压缩算法（需要指定‘w’方式，类似于open()函数传入'w'）.