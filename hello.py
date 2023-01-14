import csv

f = open('firstRec.csv', 'a', newline="")
rec1 = ('Citronpasta', 'middag')
csv.writer(f).writerow(rec1)
f.close()

f = open('firstRec.csv')
for row in csv.reader(f):
    print(row)
f.close()