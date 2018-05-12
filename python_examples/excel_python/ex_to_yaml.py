from os.path import basename
from xlrd import open_workbook


def wrap_to_dicts(rows, filepath):
  global_dict = {}
  first_key = basename(filepath).split(".")[0]
  
  curr_dict = {}
  for row in rows:
    curr_values_list = []
    if len(row) >= 1:
      key = str(row[0])
      for i in range(1, len(row)):
        if (row[i] != ''):
          curr_values_list.append(row[i])
      curr_dict[key] = curr_values_list    
  
  global_dict[first_key] = curr_dict
  # print(global_dict)
  return global_dict


def main():
  filepath = "./python_examples/excel_python/Cisco1_3850.xlsx"
  raw_from_excel = open_workbook(filepath)
  
  for sheet in raw_from_excel.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols
    # rows - is a list of lists
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
        rows.append(values)
  output_dictionary = wrap_to_dicts(rows, filepath)         


if __name__ == "__main__":
  main()
