import xlrd
import yaml

book = xlrd.open_workbook('Cisco1_3850.xlsx')
sheet = book.sheet_by_name('Global')

GlobalData = {}

# Lets 'maually' populate the Directionary. It sucks but I'm not that
# good yet with loops and Excel

system = 'system'

GlobalData[system] = {
        'hostname': sheet.cell_value(1,1),
        'timezone': sheet.cell_value(1,2),
        'recur': 'Sydney timezone',
        'fqdn': sheet.cell_value(1,4),
        'nameservers': sheet.cell_value(1,5)
        }

print(yaml.dump(GlobalData, default_flow_style=False))
