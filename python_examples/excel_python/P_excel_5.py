import xlrd

book = xlrd.open_workbook('Cisco1_3850.xlsx')
sheet = book.sheet_by_name('Global')

data = {}

# Testing some functionality
for col in range(sheet.ncols):
    cell_name = sheet.cell(0, col).value

    for row in range(1, sheet.nrows):
        if sheet.cell(col, row) != '':
            cell_data = sheet.cell(col, row).value
            data[cell_name] = cell_data

print(data)
