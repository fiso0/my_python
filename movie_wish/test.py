import csv
with open('test1.csv',newline='') as f:
    spamreader = csv.reader(f)
    for line in spamreader:
        print(line[0])
