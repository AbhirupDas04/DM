
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