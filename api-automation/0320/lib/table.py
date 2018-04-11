#-*- coding:utf-8 -*-
import xlrd

class Table(object):
	def __init__(self,excel_file):
		self.table = xlrd.open_workbook(excel_file)
		self.sheet = self.table.sheets()[0]
		self.param = self.getTableParam()

	#切换sheet页
	def changeSheet(self,sheetName):
		self.sheet = self.table.sheet_by_name(sheetName)

	#获取单元格的值
	def getCellValue(self,row,col):
		return self.sheet.cell(row - 1,ord(col) - 65).value

	#获取字段数据
	def getData(self,name,targetCol = 'C',targetRow = None):
		try:
			result = ''
			if targetRow:
				result = self.getCellValue(targetRow,targetCol)
			else:
				for i in xrange(1,self.sheet.nrows + 1):
					if name == self.getCellValue(i,'A'):
						result = self.getCellValue(i,targetCol)
						break
			return result if isinstance(result,(unicode,str)) else str(result)
		except Exception:
			return ''

	def getNum(self,str_):
		temp = ''
		for i in str_:
			if i in map(str,range(10)):
				temp = temp + i
		return temp

	def getall(self,name,targetCol = 'J'):
		result = []
		for i in xrange(1,self.sheet.nrows + 1):
			if name == self.getCellValue(i,'B'):
				temp = self.getCellValue(i,targetCol)
				result.append(temp) if isinstance(temp,(unicode,str)) else result.append(str(temp))
		return result

	def getTableParam(self):
		d = {}
		for i in self.table.sheets():
			d.update(dict([(i.name,dict(zip(i.col_values(0)[1:],i.col_values(2)[1:])))]))
		return d

# for index,i in enumerate(s.get_rows()):
# 	if index == 0:
# 		continue
# 	d[i[0].value] = i[2].value