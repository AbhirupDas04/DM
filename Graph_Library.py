WALL = 0
BOUNDARY = 1

class Graph:
    def __init__(self,max_length,max_breadth):
        self.list_edges = []
        self.max_length = max_length
        self.max_breadth = max_breadth
        self.list_vertices = [[0 for i in range(max_breadth)] for j in range(max_length)]

    def addVertice(self,x1,y1,vertex_type):
        if(self.list_vertices[x1][y1] != 0):
            return -1
        else:
            self.list_vertices[x1][y1] = Vertex(x1,y1,vertex_type)

    def addEdge(self,x1,y1,x2,y2,edge_type):
        if(self.list_vertices[x1][y1] == 0 or self.list_vertices[x2][y2] == 0):
            return -1

        if(self.list_vertices[x1][y1] in self.list_vertices[x2][y2].list_adj_vertices):
            return -1
        
        edge = Edge(self.list_vertices[x1][y1],self.list_vertices[x2][y2],edge_type)
        self.list_edges.append(edge)
        self.list_vertices[x1][y1].list_adj_vertices.append(self.list_vertices[x2][y2])
        self.list_vertices[x2][y2].list_adj_vertices.append(self.list_vertices[x1][y1])
    
class Vertex:
    def __init__(self,x_coord,y_coord,vertex_type):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.list_adj_vertices = []
        self.vertex_type = vertex_type

class Edge:
    def __init__(self,vertex_1,vertex_2,edge_type):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.edge_type = edge_type