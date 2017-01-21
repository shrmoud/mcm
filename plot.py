import csv

mylist = []
tup = ()
with open('data.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        mylist += row
        print ','.join(row)

    print mylist[0:2]
    print len(mylist)
