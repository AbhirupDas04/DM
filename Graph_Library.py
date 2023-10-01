WALL = 0
BOUNDARY = 1

class Graph:
    def __init__(self,list_vertices,list_edges):
        self.list_vertices = list_vertices
        self.list_edges = list_edges

    # def addEdge():

    
class Vertex:
    def __init__(self,x_coord,y_coord,list_adj_vertices,vertex_type):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.list_adj_vertices = list_adj_vertices
        self.vertex_type = vertex_type

class Edge:
    def __init__(self,vertex_1,vertex_2,edge_type):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.edge_type = edge_type