# cd "C:\Users\60050023\Documents\09 - Coding\DEV\MAchine learning\CodingPearls\Practice 5"

# PREREQUISITE : pip install xlrd

from os.path import basename
from xlrd import open_workbook


def wrap_to_dicts(rows, filepath):
  global_dict = {}
  first_key = basename(filepath).split(".")[0] # TODO(Bill): error handling here(if file does not exist etc.)
  
  curr_dict = {}
  for row in rows:
    curr_values_list = []
    if len(row) >= 1:     # TODO(Bill): you may want to add functionality to have key with empty value. I did not allow it.
      key = str(row[0])
      for i in range(1, len(row)):
        if (row[i] != ''):
          curr_values_list.append(row[i])
      # This will keep adding UNIQUE keys to dictionary with their values, but will override if a key already existed!
      curr_dict[key] = curr_values_list    
  
  global_dict[first_key] = curr_dict
  print(global_dict)  # This to be commented out once you are happy. 
  return global_dict

def main():
  filepath = "C:\\Users\\60050023\\Documents\\09 - Coding\\DEV\\MAchine learning\\CodingPearls\\Practice 5\\SampleGlobal.xlsx"
  raw_from_excel = open_workbook(filepath) # TODO(Bill): error handling here(if file does not exist etc.)
  
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
  '''
  for row in rows:
    print(row)
  '''
if __name__ == "__main__":
  main()
  
'''
OUTPUT:
{'SampleGlobal': {'name': ['Device1'], 'location': ['TestLocation'], 'fqdn': ['e
xample.com'], 'hosts': ['ntp1.example.com', 'ntp3.example.com', 'ntp3.example.co
m', 'dns1.example.com', 'dns3.example.com'], 'nameservers': ['10.10.10.100', '10
.20.10.100'], 'timezone': ['ADS +10'], 'recurr': ['Yes'], 'snmpro': ['ropublic']
, 'snmprw': ['rwpublic'], 'trap': ['10.30.10.100'], 'trapcommunity': ['ropublic'
]}}
'''  
