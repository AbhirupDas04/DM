from Graph_Library import *

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

for i in range(24):
    print(g1.list_vertices[i])