import csv

with open('device1_system_column.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        while row !=',': print(row['host_hosts'])
