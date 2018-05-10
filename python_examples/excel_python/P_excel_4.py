import xlrd
import yaml

book = xlrd.open_workbook('Cisco1_3850.xlsx')
sheet = book.sheet_by_name('Global')

GlobalSetting = {}

# Let's get some data off the first sheet_by_name

for i in range(1, sheet.ncols):
    hostname = sheet.cell(1, 1)

print(hostname.value)
