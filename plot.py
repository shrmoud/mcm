import csv

mylist = []
tuplist = []
#graph =  {}


with open('data.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        mylist += row
        #print ','.join(row)

   # print mylist[0:2]
   # print len(mylist)

for i in range(len(mylist)):
    #j = i+1
    start = (mylist[i].split(","))[1]
    end = (mylist[i].split(","))[2]
    tup = (start,end)
    tuplist.append(tup)
    #while(j == (len(mylist)):
          #jstart = (mylist[j].split(","))[1]
          #jend = (mylist[j].split(","))[2]

          #if(end == jend): graph[start] = ?         
          #j++
print tuplist




'''
def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges
'''

#print(generate_edges(graph))
                                     
