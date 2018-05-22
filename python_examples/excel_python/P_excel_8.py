from xlrd import open_workbook, cellname

# Initliaze a dictionary, then a list
SheetDict = {}
RowDict = {}
# First, lets open the book.
book = open_workbook('SampleBook_Column.xlsx')
sheet = book.sheet_by_name('Global')

# Assign Sheet Name to Dictionary Key
SheetDictKey = sheet.name
# Lets make sure the sheet name is a string.
while True:
    try:
        if int(SheetDictKey):
            SheetDictKey = input(
                                "Sheet must have a true name. " +
                                "Pleae enter name or 'quit' to exit.\n"
                                )
            if 'quit' in SheetDictKey.lower():
                quit()
    except ValueError:
        break

# We now try working on populating the diectionary.
for row in range(sheet.nrows):
    for col in range(1, sheet.ncols):
        if sheet.cell_value(row, col) != '':
                    RowValue = sheet.cell_value(row, 0)
                    ColValue = sheet.cell_value(row, col)
                    RowDict = {
                            RowValue: ColValue
                            }
                    SheetDict.update(RowDict)
print(SheetDict)
