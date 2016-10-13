'''
import xlrd
from xlrd import open_workbook


wb = open_workbook ("C:\\Python27\\excel\\sample1.xlsx")

sheet = wb.sheet_by_index(0)
sheetdict = {}
sheetlist = []
print sheet.nrows

for rownum in range(1,sheet.nrows):
    #sheetdict[sheet.cell(rownum,0)] = [sheet.cell(rownum,1),sheet.cell(rownum,2),sheet.cell(rownum,3)]
	sheetlist[sheet.cell(rownum,0),sheet.cell(rownum,1),sheet.cell(rownum,2),sheet.cell(rownum,3)]
	
#print sheetdict
print sheetlist
'''

from xlrd import open_workbook

class Firm(object):
    def __init__(self, name, number, balance, message):
        self.name = name
        self.number= number
        self.balance= balance
        self.message = message

    def __str__(self):
        return("Firm object:\n"
               "  Firm_Name = {0}\n"
               "  Tel_Number = {1}\n"
               "  Balance = {2}\n"
               "  Message = {3}"
               .format(self.name, self.number,
                       self.balance, self.message))

wb = open_workbook ("C:\\Python27\\excel\\sample1.xlsx")
sheet = wb.sheet_by_index(1)
number_of_rows = sheet.nrows
number_of_columns = sheet.ncols

items = []
rows = []
for row in range(1, number_of_rows):
	values = []
	for col in range(number_of_columns):
		value  = (sheet.cell(row,col).value)
		try:
			value = str(int(value))
		except ValueError:
			pass
		finally:
			values.append(value)
	item = Firm(*values)
	items.append(item)

for item in items:
    print item
    print("Accessing one single value (eg. DSPName): {0}".format(item.name))
    print
