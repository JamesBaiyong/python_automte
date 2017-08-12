#coding=utf-8


import sys,openpyxl,smtplib

wb = openpyxl.load_workbook('duesRecirds.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

lactCol = sheet.get_highest_column()
latestMonth = sheet.cell(row=1,column=lactCol).value


