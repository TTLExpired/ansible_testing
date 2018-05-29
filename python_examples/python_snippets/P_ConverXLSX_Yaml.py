from xlrd import open_workbook, cellname

# We first open the book.
book = open_workbook('SampleBook_Column.xlsx')
sheet = book.sheet_by_name('Global')

number_of_rows = sheet.nrows
number_of_columns = sheet.ncols

# Let's go through the list
rows = []
for row in range(1, number_of_rows):
    values = []
    for col in range(number_of_columns):
        value = (sheet.cell(row, col).value)
        if value != '':
            try:
                value = str(int(value))
            except ValueError:
                pass
            finally:
                values.append(value)
    rows.append(values)
print(rows)

# We now convert the created List to a Dictionary
global_dict = {}
curr_dict = {}
first_key = sheet.name

for row in rows:
    curr_values_list = []
    if len(row) >= 1:
        key = str(row[0])
        for i in range(1, len(row)):
            if (row[i] != ''):
                curr_values_list.append(row[i])
        curr_dict[key] = curr_values_list
global_dict[first_key] = curr_dict

print(global_dict)
