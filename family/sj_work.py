#encoding=utf-8
from xlrd import open_workbook
import xlwt
from xlutils.styles import Styles
import xlutils.copy
import sys

g_count = 0
g_employee_count = 0
g_header = []
g_sheet = []
g_wb = None

def generate_sheet_line(line):
	global g_sheet, g_header
	g_sheet.append(g_header)
	g_sheet.append(line)

def generate_sheet(title):
	global g_sheet, g_wb

	sheet_name = title	
	
	ws = g_wb.add_sheet(sheet_name, cell_overwrite_ok=True)
	for x in range(0, len(g_sheet)):
		for y in range(0, len(g_sheet[x])):
			ws.write(x, y, g_sheet[x][y])	

def is_number(value):	
	# Excel中看到的整数实际上是浮点型。
	return isinstance(value, float)	

def parse_sheet_line(line):
	global g_count, g_header, g_employee_count

	# 去除表头的“中心”列。
	line.pop(0)

	if g_count == 1:		
		g_header = line
		g_count = g_count + 1
		return

	# 读取第二列为纯数字的行，这是工资明细
	if is_number(line[0]):
		g_employee_count = g_employee_count + 1		
		generate_sheet_line(line)

	g_count=g_count+1

def parse_sheet(sheet, title):
	global g_count, g_header, g_sheet, g_employee_count
	# 初始化表单数据
	g_count = 0
	g_employee_count = 0
	g_header = []
	g_sheet = []

	for row in range(sheet.nrows):
		values = []
		for col in range(sheet.ncols):
			values.append(sheet.cell(row, col).value)

		parse_sheet_line(values)
	
	print(u'员工总数：'+str(g_employee_count))

	generate_sheet(title)

# 使用方法：
# 1，支持通过命令行参数传递文件名。
# 2，xls文件必须先取消密码（如果有的话）：Win下另存为时候，选择左下角“工具”。
# 3，xls文件必须是word2003兼容格式，如果不是，需要提前转换（另存为）
# 4，sheets变量修改成真正的sheets名字。 
# 5，结果输出在当前目录下，out开头的名字。
if __name__ == '__main__':	
	xls = 'gongzidan-201311-new.xls'
 	if len(sys.argv) > 1:
		xls = sys.argv[1]

	sheets = [u'2013.11（建筑）', u'2013.11(地产)']

	rb = open_workbook(xls, formatting_info=True)

	g_wb = xlwt.Workbook()

	for s in rb.sheets():
		if s.name in sheets:
			print(u'发现目标：' + s.name)
			parse_sheet(s, s.name)						

	g_wb.save('out-' + xls)
