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

for i in range(24):
    print(g1.test_bed[i])