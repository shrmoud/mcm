import csv
import networkx as nx
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt


G=nx.Graph()
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
    w = (mylist[i].split(","))[3]
    tup = (start,end)
    tuplist.append(tup)
    G.add_edge(start, end, weight=w)
    #while(j == (len(mylist)):
          #jstart = (mylist[j].split(","))[1]
          #jend = (mylist[j].split(","))[2]

          #if(end == jend): graph[start] = ?         
          #j++
#print tuplist

                              


#print("Nodes of graph: ")
#print(G.nodes())
#print("Edges of graph: ")
#print(G.edges())

nx.draw(G)
plt.savefig("weightpath.png") # save as png
plt.show() # display
