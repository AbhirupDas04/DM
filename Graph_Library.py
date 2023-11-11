import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon

WALL = 0
BOUNDARY = 1

class Graph:
    def __init__(self,max_length,max_breadth):
        self.list_edges = []
        self.max_length = max_length
        self.max_breadth = max_breadth
        self.list_vertices = [[0 for i in range(max_breadth+1)] for j in range(max_length+1)]
        self.test_bed = [[' ' for i in range(max_breadth+1)] for j in range(max_length+1)]

    def addVertice(self,x1,y1,vertex_type):
        if(self.list_vertices[y1][x1] != 0):
            return -1
        else:
            self.list_vertices[y1][x1] = Vertex(y1,x1,vertex_type)
            self.test_bed[y1][x1] = '1'

    def addEdge(self,x1,y1,x2,y2,edge_type):
        if(self.list_vertices[y1][x1] == 0 or self.list_vertices[y2][x2] == 0):
            return -1

        if(self.list_vertices[y1][x1] in self.list_vertices[y2][x2].list_adj_vertices):
            return -1
        
        edge = Edge(self.list_vertices[y1][x1],self.list_vertices[y2][x2],edge_type)
        self.list_edges.append(edge)
        self.list_vertices[y1][x1].list_adj_vertices.append(self.list_vertices[y2][x2])
        self.list_vertices[y2][x2].list_adj_vertices.append(self.list_vertices[y1][x1])
    def displayGraph(self):
        plt.title('Art Gallery')
        for edge in self.list_edges:
            x1 = edge.vertex_1.y_coord
            y1 = -edge.vertex_1.x_coord 
            x2 = edge.vertex_2.y_coord
            y2 = -edge.vertex_2.x_coord 
            plt.plot([x1, x2], [y1, y2], c='g', linewidth=1)
        plt.axis('off')
        plt.show()
    def textGenerate(path):
        
        with open(path,'r') as file:
            x = []          # list of x coordinates
            y = []          # list of y coordinates  
            k = file.readlines()
            for i in k:
                a = i.split()
                x.append(int(a[0]))
                y.append(int(a[1]))
        max_length = max(y)
        max_breadth = max(x)
        gr = Graph(max_length, max_breadth)
        #print(gr.test_bed)
        for i in range(len(x)):
            gr.addVertice(x[i], y[i], BOUNDARY)
            if i > 0:
                gr.addEdge(x[i - 1], y[i - 1], x[i], y[i], WALL)
            if i == len(x) - 1:
                gr.addEdge(x[i], y[i], x[0], y[0], WALL)
        return gr
    def onClick():
        global OCvertices, OCpolygon, OCall_vertices

        OCvertices = []
        OCpolygon = None
        OCall_vertices = []

        def on_click(event):
            global OCpolygon, OCvertices, OCall_vertices

            if event.button == 3 and OCpolygon is not None:
                # Right-click to finish drawing the polygon
                ax.add_patch(OCpolygon)
                plt.draw()
                OCall_vertices.append(OCvertices.copy()+[OCvertices[0]])
                OCvertices = []
                OCpolygon = None
            elif event.button == 1:
                # Left-click to add a vertex
                OCvertices.append((event.xdata, event.ydata))
                if len(OCvertices) > 1:
                    if OCpolygon is not None:
                        OCpolygon.remove()
                OCpolygon = Polygon(OCvertices, closed=True, edgecolor='b', facecolor='none')
                ax.add_patch(OCpolygon)
                plt.draw()

        def on_close(event):
            global OCall_vertices

            if OCall_vertices:
                gr = Graph(100, 100)
                for vertices in OCall_vertices:
                    for vertex in vertices:
                        gr.addVertice(int(vertex[0]), -int(vertex[1]), BOUNDARY)
                    for i in range(1, len(vertices)):
                        gr.addEdge(int(vertices[i - 1][0]), -int(vertices[i - 1][1]), int(vertices[i][0]), -int(vertices[i][1]), WALL)
                return gr

        fig, ax = plt.subplots()
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        fig.canvas.mpl_connect('button_press_event', on_click)
        fig.canvas.mpl_connect('close_event', on_close)
        plt.title("Draw the Layout for the Art Gallery (left_click: Pen Down, right_click: Pen Up)")
        plt.show()
        return on_close(None)
    def getList(self):
        return [j.get()[0].get() for j in self.list_edges ]


    
    
class Vertex:
    def __init__(self,x_coord,y_coord,vertex_type):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.list_adj_vertices = []
        self.vertex_type = vertex_type
    def get(self):
        return [self.y_coord, self.x_coord]
    def __str__(self):
        return f"[{self.y_coord} , {self.x_coord}]"
    
    def __repr__(self):
        return f"[{self.y_coord} , {self.x_coord}]"

class Edge:
    def __init__(self,vertex_1,vertex_2,edge_type):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.edge_type = edge_type
    def get(self):
        return [self.vertex_1, self.vertex_2]
    def __repr__(self):
        return f"({self.vertex_1} - {self.vertex_2})"