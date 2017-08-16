### 1.目录导航

**[sendDuesReminders.py](./sendDuesReminders.py)**:查找表格中特定人员，发送邮件

**[testSendMessage.py](./testSendMessage.py)**:调用发送短信模块，发送实时天气预报

**[sendMessage.py](./sendMessage.py)**:发送短信函数



### 2.发送电子邮件模块

python使用smtplib模块发送邮件,使用MIMEText函数设置文本信息

使用案例：

```pytho
import smtplib
from email.mime.text import MIMEText
```

发送邮件分为三部分，

* 邮件信息设置：电子邮件提供商的域名和端口信息，发送人邮件用户名密码，登录到邮件服务器
* 邮件文本设置：邮件发送人（From），邮件接收人(To)，文本内容(count)，主题内容(subject)
* 发送邮件：(sendmail())



### 3.Twilio发送短信

Twilio是一个SMS网关服务，在官网注册后可以使用程序向登记过的电话号码发送短信。使用前需要安装twilio模块。

* 在[官网](www.twilio.com)注册登记
* 记录下accountSID,authToken,twilio电话号码
* 调用Client发送短信

```python 
from twilio.rest import Client
...
twilioCli = Client(accountSID,authToken)	twilioCli.api.account.messages.create(body=message,from_=twilioNumber,to=myNumber)
```

