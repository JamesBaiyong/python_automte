## 处理PDF文件和World文件

### 1.目录导航

**[combinePdfs.py](./combinePdfs.py)**:合并指定文件夹中的PDF

**[decryptPDF.py](./decryptPDF.py)**:使用字典暴力破解加密的PDF文件

**[readDocx.py](./readDocx.py)**:只获取文本信息

**[readtTest.py](./readtTest.py)**:调用readDocx.py获取文本信息



### 2.PyPDF2模块

```py
import PyPDF2
pdfFileobj = open('xxx.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileobj)
```

PdfFileReader对象都有一个isEncrypted属性，检查是否加密

PdfFileReader使用getpage()方法获取到页面内容

PdfFileReader使用addpage()方法写入内容

#### 创建PDF：

模块不允许直接编辑PDF，需要创建一个心的PDF，然后从已有的文档拷贝内容

* 1.打开一个或多个PDF，得到PdfFileReader对象
* 2.创建一个新的PdfFileWriter对象
* 3.将页面从PdfFileReader对象拷贝到PdfFileWrite对象中
* 4.利用PdfFileReader对象写入输出的PDF




### 3.python-docx模块

安装pip install python-docx

```pyhton
import docx
```



#### Word文档简介 
* Document：表示整个文档
* Paragraph：表示段落
* Run：表示相同样式文本

#### Word样式
* 段落样式：可以应用于Paragraph
* 字符样式：可以应用于Run对象
* 链接样式：可以应用于Paragraph和Run对象

