import xlrd

book = xlrd.open_workbook('Cisco1_3850.xlsx')
sheet = book.sheet_by_name('Global')

data = {}

for i in range(1, sheet.nrows):
    row = sheet.row_values(i)
    data[module] = {}
    
            
