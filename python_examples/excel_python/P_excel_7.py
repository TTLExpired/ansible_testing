from xlrd import open_workbook, cellname

eval = []
RowList = []
# First, lets open the book.
book = open_workbook('SampleBook_Column.xlsx')
sheet = book.sheet_by_name('Global')

# let's practice some playing around!
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        if sheet.cell_value(row, col) != '':
            eval.append(sheet.cell_value(row, col))
    RowList.append(eval)
    eval = []

# Let's Print the overall List
for value in range(len(RowList)):
    print(RowList[value])
