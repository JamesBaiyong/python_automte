### 1.目录导航

**[multiplicationTable.py](./multiplicationTable.py)**:用命令行执行该程序，指定数字返回一个N X N的乘法表

**[readCensusExcel.py](./readCensusExcel.py)**:从电子表格读取数据

**[sampleChart.py](./sampleChart.py)**:制作图表

**[updateProduce.py](./updateProduce.py)**:更新电子表格中的数据



### 2.openpyxl模块

#### 从电子表格文件中读取单元格涉及的所有函数，方法，数据类型。

1. 导入 openpyxl 模块。
2. 调用 openpyxl.load_workbook()函数。
3. 取得 Workbook 对象。
4. 调用 get_active_sheet()或 get_sheet_by_name()工作簿方法。
5. 取得 Worksheet 对象。
6. 使用索引或工作表的 cell()方法，带上 row 和 column 关键字参数。
7. 取得 Cell 对象。
8. 读取 Cell 对象的 value 属性。

#### 

openpyxl.load_workbook('example.xlsx')：返回一个workbook数据类型的值，代表这个excel文件

get_sheet_names()：取得工作簿中所有表名的列表，每个表由worksheet对象表示

 create_sheet_names():返回一个新的worksheet对象，默认是工作簿的最后一个表，可用index关键字创建索引

单元格公式：

```py
 import openpyxl
 wb = openpyxl.Workbook()
 sheet = wb.get_active_sheet()
 sheet['A1'] = 200
 sheet['A2'] = 200
 sheet['A3'] = '=SUM(A1:A2)'
 wb.save('write.xlsx')
```



