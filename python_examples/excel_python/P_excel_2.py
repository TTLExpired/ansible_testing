import xlrd

book = xlrd.open_workbook('Cisco1_3850.xlsx')
sheet = book.sheet_by_name('Global')

data = {}

for i in range(1, sheet.nrows):
    # Assign row a LIST of Excel row
    row = sheet.row_values(i)
    # Print the number and the row
    print(i, row) 
    # We now the first index is the module, get that.
    module = row[0]
    # now assign it to dictionary. Note that will be repeaterd for times
    # However, the last 3 times are empty so Python only records it once
    data[module] = {}

print('the module is: ', data)
