## 网页抓取信息

### 1.文件导航

**文件[downloadXKCD.py](./downloadXKCD.py)**:下载XKCD上的极客漫画



### 2.webbrower

open()函数可以启动一个新浏览器，打开指定的URL。

```python
import webbrower
webbrower.open('http://www.163.com')
```



### 3.requests

用于从web上下载文件和网页，不用担心网络错误，链接，数据压缩等问题。

*下载页面和检查错误

```python
import requests
res = requests.get(URL)
res.rase_for_status()#下载文件出错则抛出异常，否则什么都不做
```



### 4.BeautifulSoup

用于从HTML页面中提取信息，模块名称是bs4





### 5.Selenium

启动并控制浏览器

*启动控制浏览器

```py
from selenium import webdriver
brower = webdriver.Firefox()
brower.get(URL)
```



*页面中寻找元素

