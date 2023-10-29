from Graph_Library import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
from scipy.spatial import ConvexHull
g1 = Graph(23,24)

for i in range(25):
    g1.addVertice(i,23,BOUNDARY)

for i in range(10,24):
    g1.addVertice(0,i,BOUNDARY)

for i in range(1,6):
    g1.addVertice(i,10,BOUNDARY)

for i in range(11,17):
    g1.addVertice(5,i,BOUNDARY)

for i in range(16,5,-1):
    g1.addVertice(6,i,BOUNDARY)

g1.addVertice(5,7,BOUNDARY)
g1.addVertice(4,8,BOUNDARY)
g1.addVertice(3,7,BOUNDARY)
g1.addVertice(2,6,BOUNDARY)
g1.addVertice(1,6,BOUNDARY)

for i in range(6,2,-1):
    g1.addVertice(0,i,BOUNDARY)

for i in range(0,5):
    g1.addVertice(i,3,BOUNDARY)

g1.addVertice(4,2,BOUNDARY)
g1.addVertice(4,1,BOUNDARY)

for i in range(4,14):
    g1.addVertice(i,0,BOUNDARY)

g1.addVertice(13,1,BOUNDARY)
g1.addVertice(13,2,BOUNDARY)
g1.addVertice(14,2,BOUNDARY)
g1.addVertice(15,2,BOUNDARY)
g1.addVertice(15,1,BOUNDARY)

for i in range(15,19):
    g1.addVertice(i,0,BOUNDARY)

g1.addVertice(19,1,BOUNDARY)
g1.addVertice(20,2,BOUNDARY)
g1.addVertice(21,1,BOUNDARY)

for i in range(5):
    g1.addVertice(22,i,BOUNDARY)

for i in range(21,17,-1):
    g1.addVertice(i,4,BOUNDARY)

x = 19
y = 5
for i in range(3):
    g1.addVertice(x,y,BOUNDARY)
    x+=1
    y+=1

for i in range(20,14,-1):
    g1.addVertice(i,7,BOUNDARY)

x = 16
y = 8
for i in range(3):
    g1.addVertice(x,y,BOUNDARY)
    x+=1
    y+=1

x = 19
y = 10
for i in range(3):
    g1.addVertice(x,y,BOUNDARY)
    x+=1
    y-=1

for i in range(7,13):
    g1.addVertice(22,i,BOUNDARY)    

for i in range(21,13,-1):
    g1.addVertice(i,12,BOUNDARY)

g1.addVertice(14,13,BOUNDARY)

for i in range(14,9,-1):
    g1.addVertice(i,14,BOUNDARY)

for i in range(15,20):
    g1.addVertice(10,i,BOUNDARY)

for i in range(11,25):
    g1.addVertice(i,19,BOUNDARY)

for i in range(20,23):
    g1.addVertice(24,i,BOUNDARY)

x = 7
y = 3
for i in range(5):
    g1.addVertice(x,y,WALL)
    x+=1
    y+=1

x = 14
y = 5
for i in range(3):
    g1.addVertice(x,y,WALL)
    x+=1
    y-=1

for i in range(3,7):
    g1.addVertice(i,18,WALL)

g1.addVertice(3,19,WALL)
g1.addVertice(3,20,WALL)
g1.addVertice(6,19,WALL)
g1.addVertice(6,20,WALL)
g1.addVertice(4,20,WALL)
g1.addVertice(5,20,WALL)

list_edges = []

for i in range(4,13):
    list_edges.append([i,0,i+1,0,BOUNDARY])

list_edges.append([13,0,13,1,BOUNDARY])
list_edges.append([13,1,13,2,BOUNDARY])
list_edges.append([13,2,14,2,BOUNDARY])
list_edges.append([14,2,15,2,BOUNDARY])
list_edges.append([15,2,15,1,BOUNDARY])
list_edges.append([15,1,15,0,BOUNDARY])

for i in range(15,18):
    list_edges.append([i,0,i+1,0,BOUNDARY])

list_edges.append([18,0,19,1,BOUNDARY])
list_edges.append([19,1,20,2,BOUNDARY])
list_edges.append([20,2,21,1,BOUNDARY])
list_edges.append([21,1,22,0,BOUNDARY])

for i in range(0,4):
    list_edges.append([22,i,22,i+1,BOUNDARY])

for i in range(22,18,-1):
    list_edges.append([i,4,i-1,4,BOUNDARY])

x = 18
y = 4
for i in range(3):
    list_edges.append([x,y,x+1,y+1,BOUNDARY])
    x+=1
    y+=1

for i in range(21,15,-1):
    list_edges.append([i,7,i-1,7,BOUNDARY])

x = 15
y = 7
for i in range(3):
    list_edges.append([x,y,x+1,y+1,BOUNDARY])
    x+=1
    y+=1

list_edges.append([18,10,19,10,BOUNDARY])

x = 19
y = 10
for i in range(3):
    list_edges.append([x,y,x+1,y-1,BOUNDARY])
    x+=1
    y-=1

for i in range(7,12):
    list_edges.append([22,i,22,i+1,BOUNDARY])

for i in range(22,14,-1):
    list_edges.append([i,12,i-1,12,BOUNDARY])

list_edges.append([14,12,14,13,BOUNDARY])
list_edges.append([14,13,14,14,BOUNDARY])

for i in range(14,10,-1):
    list_edges.append([i,14,i-1,14,BOUNDARY])

for i in range(14,19):
    list_edges.append([10,i,10,i+1,BOUNDARY])

for i in range(10,24):
    list_edges.append([i,19,i+1,19,BOUNDARY])

for i in range(19,23):
    list_edges.append([24,i,24,i+1,BOUNDARY])

for i in range(24,0,-1):
    list_edges.append([i,23,i-1,23,BOUNDARY])

for i in range(23,10,-1):
    list_edges.append([0,i,0,i-1,BOUNDARY])

for i in range(5):
    list_edges.append([i,10,i+1,10,BOUNDARY])

for i in range(10,16):
    list_edges.append([5,i,5,i+1,BOUNDARY])

list_edges.append([5,16,6,16,BOUNDARY])

for i in range(16,6,-1):
    list_edges.append([6,i,6,i-1,BOUNDARY])

list_edges.append([6,6,5,7,BOUNDARY])
list_edges.append([5,7,4,8,BOUNDARY])
list_edges.append([4,8,3,7,BOUNDARY])
list_edges.append([3,7,2,6,BOUNDARY])
list_edges.append([2,6,1,6,BOUNDARY])
list_edges.append([1,6,0,6,BOUNDARY])

for i in range(6,3,-1):
    list_edges.append([0,i,0,i-1,BOUNDARY])

for i in range(4):
    list_edges.append([i,3,i+1,3,BOUNDARY])

for i in range(3,0,-1):
    list_edges.append([4,i,4,i-1,BOUNDARY])

x = 7
y = 3
for i in range(4):
    list_edges.append([x,y,x+1,y+1,WALL])
    x+=1
    y+=1

list_edges.append([14,5,15,4,WALL])
list_edges.append([15,4,16,3,WALL])
list_edges.append([3,18,3,19,WALL])
list_edges.append([3,19,3,20,WALL])
list_edges.append([6,18,6,19,WALL])
list_edges.append([6,19,6,20,WALL])

for i in range(3,6):
    list_edges.append([i,18,i+1,18,WALL])

for i in range(3,6):
    list_edges.append([i,20,i+1,20,WALL])

for i in list_edges:
    g1.addEdge(i[0],i[1],i[2],i[3],i[4])

# print(g1.list_vertices[0][4].list_adj_vertices)

#print(g1.list_edges)
#print(g1.test_bed)
# for i in range(24):
#     print(g1.test_bed[i])


#print(g1.list_vertices)
# data i hv 
# test bed
# list of vertices
#list of edges
# algorithm : first plot all the vertices out; then iterate through all the edges and connect accordingly
#g1.displayGraph()



#to take input from the user and convert it to the graph format
#rando
#list of edges and vertices either cli or txt file


#   Case 1:      rando


#    case 2: from a text file containing the coordinates
#Graph.displayGraph(Graph.textGenerate(r"testInput.txt"))

# case 3 : based on drawing on a screen
#lets do it using pygame(interactive screen)
x = Graph.onClick()
x.displayGraph()