### 1.文件导航

**[stopwatch.py](./stopwatch.py)**:超级秒表，记录每一圈用时和总共用时

**[multidownloadXkcd.py](./multidownloadXkcd.py)**:多进程下载XKCD上的极客漫画

**[countdown.py](./countdown.py)**:定时打开文件



### 2.time模块

用于取得Unix纪元时间戳，并加以处理。

#### time.time()函数

time.time()返回自协调世界时那一刻以来的秒数，是一个浮点值，这个数字成为UNIX纪元时间戳。

可以使用该函数做简单的记时功能

#### time.sleep()函数

time.sleep()函数使程序暂停传入的时间秒数。



### 3.datetime模块

datetime模块有自己的datetime数据类型，datetime值表示一个特定的时刻。

#### datetime.datetime.now()

返回一个datetime对象，表示当前的日期合时间，包含当前时刻的年月日时分秒微秒。

#### datetime.datetime()

可以传入代表年月日时分秒的整数，得到特定时刻的datetime对象。这些整数将保存在datetime对象的year，month，day，hour，minute，second属性中。

#### datetime.datetime.fromtimestamp()

传入整数，返回datetime对象，表示Unix纪元后整数秒的时刻。传入tiem.time()将返回当前时刻的datetime对象。

#### timedelta数据类型

表示一段时间，而不是一个时刻。

datetime.timedelta()函数，创建timedelta对象。

#### 将datetime对象转换为字符串

利用strftime()方法，可以将datetime对象显示为字符串。

格式化字符串意义：

- %y 两位数的年份表示（00-99）
- %Y 四位数的年份表示（000-9999）
- %m 月份（01-12）
- %d 月内中的一天（0-31）
- %H 24小时制小时数（0-23）
- %I 12小时制小时数（01-12）
- %M 分钟数（00=59）
- %S 秒（00-59）
- %a 本地简化星期名称
- %A 本地完整星期名称
- %b 本地简化的月份名称
- %B 本地完整的月份名称
- %c 本地相应的日期表示和时间表示
- %j 年内的一天（001-366）
- %p 本地A.M.或P.M.的等价符
- %U 一年中的星期数（00-53）星期天为星期的开始
- %w 星期（0-6），星期天为星期的开始
- %W 一年中的星期数（00-53）星期一为星期的开始
- %x 本地相应的日期表示
- %X 本地相应的时间表示
- %Z 当前时区的名称
- %% %号本身

#### 将字符串转换成datetime对象

strptime()函数将字符串转换成datetime对象，同样需要传入格式化字符串。



### 4.多线程

要得到单独的县城，首先调用threading.Thread()函数，生成Thread对象。当创建一个新的Thread对象时，要确保其目标函数只使用该函数中的局部变量。避免程序中难以调试的并发问题。

