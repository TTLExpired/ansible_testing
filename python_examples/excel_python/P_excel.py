import xlrd

book = xlrd.open_workbook('Cisco1_3850.xlsx')


for sheet in book.sheets():
    print ( sheet.name )
