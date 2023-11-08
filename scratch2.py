
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
def calculate_angle(p1, p2, p3):
    vector1 = [p2[0] - p1[0], p2[1] - p1[1]]
    vector2 = [p3[0] - p2[0], p3[1] - p2[1]]

    dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]
    magnitude1 = math.hypot(vector1[0], vector1[1])
    magnitude2 = math.hypot(vector2[0], vector2[1])

    if magnitude1 < 1e-6 or magnitude2 < 1e-6:
        return 0
    angle_cosine = dot_product / (magnitude1 * magnitude2)

    angle_cosine = min(1.0, max(-1.0, angle_cosine))

    angle_deg = math.degrees(math.acos(angle_cosine))
    return angle_deg

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
            ear = Polygon([prev, curr, next])
            if main_poly.contains(ear):
                triangles.append(ear)
                dummylist.pop(i)
                break

    for triangle in triangles:
        main_poly = main_poly.difference(triangle)

    # Extract vertices from each triangle and store them in a list
    triangle_vertices = []
    for triangle in triangles:
        triangle_vertices.append(list(triangle.exterior.coords))

    return main_poly, triangle_vertices

def plot_polygon_and_triangles(main_polygon, triangle_vertices):
    fig, ax = plt.subplots()

    # Plot the main polygon
    x, y = main_polygon.exterior.xy
    ax.fill(x, y, alpha=0.5, color='blue', edgecolor='black')

    # Plot the triangles as a list of vertices
    for vertices in triangle_vertices:
        x, y = zip(*vertices)  # Separate x and y coordinates
        ax.fill(x, y, alpha=0.5, color='green', edgecolor='black')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Main Polygon with Triangles (List of Vertices)')
    plt.show()


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
    



dummylist = [[21,-83],[9,-71],[8 , -59],[20 , -73],[5 , -47],[12 , -47],[24 , -56],[4 , -25],[36 , -14],[72 , -31],[71 , -58],[71 , -77],[83 , -84],[82 , -89],[68 , -83],[64 , -92],[51 , -93],[48 , -83],[45 , -93],[51 , -96],[28 , -95],[19 , -92]]
print(len(dummylist))
main_polygon, triangle_vertices = triangulate(dummylist)
print(triangle_vertices)
print(count_guards(triangle_vertices))
plot_polygon_and_triangles(main_polygon, triangle_vertices)


