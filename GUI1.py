import tkinter
from tkinter import *
from PIL import Image,ImageTk
from Triangulation import Triangulation
from Graph_Library import Graph
from shapely.geometry import Polygon
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GUI:
    def __init__(self,root):
        #Main variables
        self.mainPolygon = ''
        self.triangleVerts = []
        self.minGuardList = []
        self.vertList = []
        self.path = ""
        self.filtered_minGuardList = []

        
        # Setting Up
        self.root = root
        self.root.geometry('400x600')
        self.root.resizable(False,False)
        self.root.title('Art Gallery Problem')
        self.icon = ImageTk.PhotoImage(Image.open('icon.png'))
        root.iconphoto(False,self.icon)
        self.mainCanvas = tkinter.Canvas(root,bg = '#363636',width=400,height=600,highlightthickness=0)
        self.previewFrame = tkinter.Frame(root,bg = '#4d4c4c',width=300,height=450,borderwidth=1)
        self.previewFrame.place(x=25,y=10)
        self.fig, self.ax = plt.subplots(figsize=(3.5,4), tight_layout=True)
        self.ax.axis('off')
    
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.previewFrame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill='both', expand=True)


        self.OnclickButton = tkinter.Button(root,text='OnClick',bg='#434343',activebackground='#434343',padx=100,command = self.OnClick)
        self.txtButton = tkinter.Button(root,text="Load .txt File",bg='#434343',activebackground='#434343',padx=87,command = self.txtGenerate)
        self.Clear = tkinter.Button(root,text="Clear",bg='#434343',activebackground='#434343',padx=108,command = self.clear)
        self.generate = tkinter.Button(root,text="Generate",bg='#434343',activebackground='#434343',padx=50,command = self.Generate)
        self.quit = tkinter.Button(root,text="Quit",bg="#434343",activebackground='#434343',command = root.quit)

        self.mainCanvas.create_window(80,455,anchor='sw',window=self.OnclickButton)
        self.mainCanvas.create_window(80,485,anchor='sw',window=self.txtButton)
        self.mainCanvas.create_window(80,515,anchor='sw',window=self.Clear)
        self.mainCanvas.create_window(70,575,anchor='sw',window=self.generate)
        self.mainCanvas.create_window(290,575,anchor='sw',window=self.quit)

        self.mainCanvas.pack(fill='both',expand=True)

    #function for displaying the current graph onto the previewFrame 
    def preview(self):
        self.ax.clear()

        # Plot the mainPolygon
        if self.mainPolygon:
            '''
            polygon = Polygon(self.mainPolygon.list_vertices)
            x, y = polygon.exterior.xy
            self.ax.plot(x, y, color='blue', linewidth=2, alpha=0.7)'''
            for edge in self.mainPolygon.list_edges:
                x1 = edge.vertex_1.y_coord
                y1 = -edge.vertex_1.x_coord 
                x2 = edge.vertex_2.y_coord
                y2 = -edge.vertex_2.x_coord 
                self.ax.plot([x1, x2], [y1, y2], c='g', linewidth=1,alpha=0.7)
        self.ax.axis('off')
        self.ax.set_title('Preview')
        self.canvas.draw()

    # Function for initializing the onClick() function from the Graph library
    def OnClick(self):
        self.mainPolygon = Graph.onClick()
        print(self.mainPolygon.list_edges)
        self.preview()
        
    # Function for initializing the textGenerate() function from the Graph library
    def txtGenerate(self):
        self.path = askopenfilename()
        print(self.path)
        if self.path == '':
            return 
        self.mainPolygon = Graph.textGenerate(self.path)
        print(self.mainPolygon.list_edges)
        self.preview()

        
    # Function for clearing the current selection
    def clear(self):
        self.mainPolygon = ''
        self.path = ''
        self.triangleVerts = []
        self.minGuardList = []
        self.vertList = []
        self.filtered_minGuardList = []
        self.ax.clear()
        self.ax.axis('off')
        self.ax.set_title('Preview')
        self.canvas.draw()

    # Function for generating the triangulation and finding the optimal positions for the guards using Triangulation.OptimizedGuardCount
    def Generate(self):
        if self.mainPolygon:
            self.vertList = self.mainPolygon.getList()
            print(self.vertList)
            main, self.triangleVerts, self.minGuardList = Triangulation.OptimizedGuardCount(self.vertList)
            if len(self.minGuardList) == 1:
                Triangulation.plot_polygon_and_triangles(main, self.triangleVerts, self.minGuardList[0])
            for i in range(len(self.minGuardList)):
                points = []
                for j in self.minGuardList[i]:
                    points.append((j[0],j[1]))
                self.minGuardList[i] = points
            self.minGuardList = [set(i) for i in self.minGuardList]
            print(self.minGuardList)
            for i in self.minGuardList:
                if self.minGuardList.count(i) >= 2 and (i not in self.filtered_minGuardList):
                    self.filtered_minGuardList.append(i)
            print("Updated MINGUARDLIST:", self.filtered_minGuardList)
            for i in self.filtered_minGuardList:
                Triangulation.plot_polygon_and_triangles(main, self.triangleVerts, list(i))  
