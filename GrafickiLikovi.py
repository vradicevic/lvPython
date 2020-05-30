import tkinter as tk
import tkinter.ttk as ttk


class GrafLik:
    tocke =[ 0.0, 0.0]
    boja = "white"

    def SetColor(self,color):
        self.boja = color
    def GetColor(self):
        return self.boja
    def Draw(self, canvas):
        canvas




class Line(GrafLik):
    tocke = [0.0,0.0,0.0,0.0]
    boja = "white"

    def __init__(self, tocke, color):
        self.tocke = tocke
        self.boja = color

    def Draw(self,canvas):
        canvas.create_line(*self.tocke, fill = self.boja)

    
    
    


