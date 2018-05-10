import xlrd
import yaml

book = xlrd.open_workbook('Cisco1_3850.xlsx')
sheet = book.sheet_by_name('Global')

system = 'system'
GlobalData = {}

for i in range(1, sheet.nrows):
    row = sheet.row_values(i)

    if row[1] != '':
        print(row[1])

        GlobalData[system] = {
                    'Hostname:': row[1],
                    'tz': row[2],
                    'recur': 'ADST recurring 1 Sun Oct 2:00 1 Sun Apr 3:00',
                    'fqdn': row[4],
                    'name_server': [row[5]]
                }

print(yaml.dump(GlobalData, default_flow_style=False))
