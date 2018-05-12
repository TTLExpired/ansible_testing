import xlrd
import pudb

book = xlrd.open_workbook('Cisco1_3850.xlsx')
sheet = book.sheet_by_name('Global')

data = {}

# Testing some functionality

pudb.set_trace()
for col in range(sheet.ncols):
    cell_name = sheet.cell(0, col).value
    print(cell_name)

    for row in range(1, sheet.nrows):
        cell_data = sheet.cell(col, row).value
        print(cell_data)

        if cell_data !='':
            cell_data = sheet.cell(col, row).value
            data[cell_name] = cell_data

print(data)
