import csv

# with open('device1_system_raws.csv') as csvfile:
    # readfile = csv.reader(csvfile, delimiter=',', quotechar='"')
    # for row in readfile:
        # if row:
            # print(row[0], row[1], row[2])


with open('device1_global_M_1_row.csv') as csvfile:
    readfile = csv.DictReader(csvfile)
    for row in readfile:
        print(row)
        print(row['hostname'])
        print('hostname: ' + row['RadiusGroup'])
