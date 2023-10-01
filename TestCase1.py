WALL_VERTEX = 0
BOUNDARY_VERTEX = 1

class Vertex:
    def __init__(self,x_coord,y_coord,list_adj_vertices,vertex_type):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.list_adj_vertices = list_adj_vertices
        self.vertex_type = vertex_type

class Edge:
    def __init__(self,vertex_1,vertex_2):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2