import tkinter as tk
import tkinter.ttk as ttk
import math


class GrafLik:
    tocke =[ 0.0, 0.0]
    boja = "white"
    def __init__(self, tocke, color):
        self.tocke = tocke
        self.boja = color

    def SetColor(self,color):
        self.boja = color
    def GetColor(self):
        return self.boja
    def Draw(self, canvas):
        canvas




class Line(GrafLik):
    tocke = [0.0,0.0,0.0,0.0]
    boja = "white"
    

    def Draw(self,canvas):
        canvas.create_line(*self.tocke, fill = self.boja)


class Triangle(Line):
    
    def Draw(self,canvas):
        canvas.create_line(*self.tocke[0:4],fill= self.boja)
        canvas.create_line(*self.tocke[2:],fill=self.boja)
        canvas.create_line(*self.tocke[0:2],*self.tocke[4:],fill=self.boja)

class Polygon(GrafLik):

    def Draw(self,canvas):
        canvas.create_polygon(*self.tocke, outline = self.boja, fill = '')


class Rectangle(GrafLik):
    def Draw(self,canvas):
        canvas.create_rectangle(*self.tocke[0:2],self.tocke[0]-self.tocke[3],self.tocke[1]-self.tocke[2], outline = self.boja, fill = '')



class Circle(GrafLik):
    
    def Draw(self,canvas):
        canvas.create_oval(self.tocke[0]-self.tocke[2],
                           self.tocke[1]+self.tocke[2],
                           self.tocke[0]+self.tocke[2],
                           self.tocke[1]-self.tocke[2],
                           outline = self.boja,
                           fill='')


class Ellipse(Circle):

    def Draw(self,canvas):
        canvas.create_oval(self.tocke[0]-self.tocke[2],
                           self.tocke[1]+self.tocke[3],
                           self.tocke[0]+self.tocke[2],
                           self.tocke[1]-self.tocke[3],
                           outline = self.boja,
                           fill='')