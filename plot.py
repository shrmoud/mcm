import csv
import networkx as nx
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt


G=nx.Graph()
mylist = []
tuplist = []

with open('data.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        mylist += row
        #print ','.join(row)

   # print mylist[0:2]
   # print len(mylist)

for i in range(len(mylist)):
    mysplit = mylist[i].split(",")
   #print mysplit
    start = mysplit[1]
    end = mysplit[2]
    w = (int(mysplit[3])/100000)
    #print type(w)
    tup = (start,end)
    tuplist.append(tup)
    #G.add_edge(start, end)#, weight= (w/1000))
    G.add_edge(start,end,color='red',weight=w,size=10)
    
print("Length of tuple list")
print (len(tuplist))
                            

print("Number of Nodes of graph: ")
print(len(G.nodes()))
print("Number of Edges of graph: ")
print(len(G.edges()))

nx.draw(G)
plt.savefig("edges.png") # save as png
plt.show() # display
