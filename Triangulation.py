
'''
from shapely.geometry import Polygon

polya = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)]) 
polyb = Polygon([(0.5, 0.5), (0.5, 0.8), (0.8, 0.8), (0.8, 0.5)]) 

polya.contains(polyb)
https://stackoverflow.com/questions/55840924/how-to-judge-if-a-polygon-is-inside-another-polygon-in-python
'''


from shapely.geometry import Polygon
import math
import matplotlib.pyplot as plt

class Triangulation:
    # for showing a plot diagram of the triangulated polygon
    def plot_polygon_and_triangles(main_polygon, triangle_vertices,guardPos=[]):
        fig, ax = plt.subplots()

        # Plot the main polygon
        x, y = main_polygon.exterior.xy
        ax.fill(x, y, alpha=0.5, color='blue', edgecolor='black')

        # Plot the triangles as a list of vertices
        for vertices in triangle_vertices:
            x, y = zip(*vertices)  
            ax.fill(x, y, alpha=0.5, color='green', edgecolor='black')
            plt.title("After triangulating the Art Gallery")
        if guardPos:
            x, y = zip(*guardPos) 
            ax.scatter(x, y, color='red', marker='H', label='Guard Positions')
            plt.title("Optimal positions of Guards")
        plt.axis('off')  
        plt.show()
    
    #for triangulating the polygon
    def triangulate(dummylist):
        if len(dummylist) < 3:
            print("Insufficient plots")
            return None

        main_poly = Polygon(dummylist)
        triangles = []

        while len(dummylist) > 2:
            for i in range(len(dummylist)):
                prev = dummylist[i - 1]
                curr = dummylist[i]
                next = dummylist[(i + 1) % len(dummylist)]

                # Check for duplicate vertices
                if (prev, curr, next) in triangles:
                    dummylist.pop(i)
                    break

                try:
                    m = (prev[1] - curr[1]) / (prev[0] - curr[0])
                    n = (curr[1] - next[1]) / (curr[0] - next[0])
                    if m == n:
                        dummylist.pop(i)
                        break
                except ZeroDivisionError:
                    if (prev[0] == curr[0] and next[0] == curr[0]) or (prev[1] == curr[1] and next[1] == curr[1]):
                        dummylist.pop(i)
                        break

                ear = Polygon([prev, curr, next])
                if main_poly.contains(ear):
                    triangles.append((prev, curr, next))
                    dummylist.pop(i)
                    break
                else:
                    if len(dummylist) == 3:
                        break

        for triangle in triangles:
            main_poly = main_poly.difference(Polygon(triangle))

        # Extract vertices from each triangle and store them in a list
        triangle_vertices = [list(triangle) for triangle in triangles]

        # Plot the triangles
        #fig, ax = plt.subplots()
        #x, y = main_poly.exterior.xy
        #ax.fill(x, y, alpha=0.5, color='blue', edgecolor='black')

        #for triangle in triangle_vertices:
        #    triangle.append(triangle[0])  # Close the triangle
        #    x, y = zip(*triangle)
        #   ax.plot(x, y, color='red')

        #plt.show()

        return main_poly, triangle_vertices
    
    #for counting the number of gaurds and their location in the polygon

    def count_guards(triangle_vertices):
        a=[]
        b=[]
        c=[]
    
        for i in triangle_vertices: 
            x = i[0]
            y = i[1]
            z = i[2]
        
            if x in a or x in b or x in c:
                pass
            else:
                if y in a:
                    if z in b:
                        c.append(x)
                    elif z in c:
                        b.append(x)
                    else:
                        b.append(x)
                elif y in b:
                    if z in a:
                        c.append(x)
                    elif z in c:
                        a.append(x)
                    else:
                        a.append(x)
                elif y in c:
                    if z in b:
                        a.append(x)
                    elif z in a:
                        b.append(x)
                    else:
                        a.append(x)
                elif z in a:
                    if y in b:
                        c.append(x)
                    elif y in c:
                        b.append(x)
                    else:
                        b.append(x)
                elif z in b:
                    if y in a:
                        c.append(x)
                    elif y in c:
                        a.append(x)
                    else:
                        a.append(x)
                elif z in c:
                    if y in b:
                        a.append(x)
                    elif y in a:
                        b.append(x)
                    else:
                        a.append(x)
                else:
                    a.append(x)
        
            if y in a or y in b or y in c:
                pass
            else:
                if x in a:
                    if z in b:
                        c.append(y)
                    elif z in c:
                        b.append(y)
                    else:
                        b.append(y)
                elif x in b:
                    if z in a:
                        c.append(y)
                    elif z in c:
                        a.append(y)
                    else:
                        a.append(y)
                elif x in c:
                    if z in b:
                        a.append(y)
                    elif z in a:
                        b.append(y)
                    else:
                        a.append(y)
                elif z in a:
                    if x in b:
                        c.append(y)
                    elif x in c:
                        b.append(y)
                    else:
                        b.append(y)
                elif z in b:
                    if x in a:
                        c.append(y)
                    elif x in c:
                        a.append(y)
                    else:
                        a.append(y)
                elif z in c:
                    if x in b:
                        a.append(y)
                    elif x in a:
                        b.append(y)
                    else:
                        a.append(y)
                else:
                    a.append(y)        
        
            if z in a or z in b or z in c:
                pass
            else:
                if y in a:
                    if x in b:
                        c.append(z)
                    elif x in c:
                        b.append(z)
                    else:
                        b.append(z)
                elif y in b:
                    if x in a:
                        c.append(z)
                    elif x in c:
                        a.append(z)
                    else:
                        a.append(z)
                elif y in c:
                    if x in b:
                        a.append(z)
                    elif x in a:
                        b.append(z)
                    else:
                        a.append(z)
                elif x in a:
                    if y in b:
                        c.append(z)
                    elif y in c:
                        b.append(z)
                    else:
                        b.append(z)
                elif x in b:
                    if y in a:
                        c.append(z)
                    elif y in c:
                        a.append(z)
                    else:
                        a.append(z)
                elif x in c:
                    if y in b:
                        a.append(z)
                    elif y in a:
                        b.append(z)
                    else:
                        a.append(z)
                else:
                    a.append(z)            
    
        guards =[]
        guards.append(len(a))
        guards.append(len(b))
        guards.append(len(c))
        min_guards = min(guards)
        if min_guards == len(a):
            return a
        elif min_guards == len(b):
            return b
        elif min_guards == len(c):
            return c
    def OptimizedGuardCount(vertList):
        guardCountDict = {}
        min_ = len(vertList)
        for i in range(len(vertList)):
            currCycle = vertList[i::]+vertList[:i]
            main,triangleVert = Triangulation.triangulate(currCycle)
            #Triangulation.plot_polygon_and_triangles(main,triangleVert)
            a = Triangulation.count_guards(triangleVert)
            if min_ >= len(a):
                min_ = len(a)
            #print(min_)
            if len(a) not in guardCountDict.keys():
                guardCountDict[len(a)] = [a]
            else:
                guardCountDict[len(a)] = guardCountDict[len(a)] +[a]
                #print(a)
        #for i in guardCountDict.keys():
        #    print("Guard count",i)
        #   print("\t\t",guardCountDict[i])
        return main,triangleVert,guardCountDict[min_]
