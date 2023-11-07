from shapely.geometry import Polygon
import math
import matplotlib.pyplot as plt
'''
from shapely.geometry import Polygon

polya = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)]) 
polyb = Polygon([(0.5, 0.5), (0.5, 0.8), (0.8, 0.8), (0.8, 0.5)]) 

polya.contains(polyb)
https://stackoverflow.com/questions/55840924/how-to-judge-if-a-polygon-is-inside-another-polygon-in-python
'''

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
        return []
    triangles = []
    while len(dummylist) > 2:
        main_poly = Polygon(dummylist)
        for i in range(len(dummylist)):
            prev = dummylist[i - 1]
            curr = dummylist[i]
            next = dummylist[(i + 1) % len(dummylist)]
            ear = Polygon([prev, curr, next])
            if main_poly.contains(ear):
                triangles.append(ear)
                dummylist.pop(i)
                break
    return triangles

def plot_polygon_and_triangles(original_polygon, triangles):
    fig, ax = plt.subplots()

    # Plot the original polygon
    x, y = original_polygon.exterior.xy
    ax.fill(x, y, alpha=0.5, color='blue', edgecolor='black')

    # Plot the triangulated triangles
    for triangle in triangles:
        x, y = triangle.exterior.xy
        ax.fill(x, y, alpha=0.5, color='green', edgecolor='black')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Original Polygon and Triangles')
    plt.show()

dummylist = [[10, -78], [12, -17], [80, -23], [78, -88], [64, -87], [67, -37], [30, -32], [28, -44], [43, -48], [43, -84], [10, -79]]
p = Polygon(dummylist)
triangles = triangulate(dummylist)

plot_polygon_and_triangles(p, triangles)