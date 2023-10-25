import matplotlib.pyplot as plt
import matplotlib.patches as patches

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


        '''
        #Displaying the generated graph
        plt.scatter(x, y, marker='o', color='g', label='Data Points')
        polygon = patches.Polygon(list(zip(x, y)), closed=True, fill=None, edgecolor='g', lw=2, label='Polygon Border')
        plt.gca().add_patch(polygon)
        plt.title('From text file')
        plt.axis('off')
        plt.show()'''

    
class Vertex:
    def __init__(self,x_coord,y_coord,vertex_type):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.list_adj_vertices = []
        self.vertex_type = vertex_type

    def __str__(self):
        return f"[{self.y_coord} , {self.x_coord}]"
    
    def __repr__(self):
        return f"[{self.y_coord} , {self.x_coord}]"

class Edge:
    def __init__(self,vertex_1,vertex_2,edge_type):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.edge_type = edge_type

    def __repr__(self):
        return f"({self.vertex_1} - {self.vertex_2})"