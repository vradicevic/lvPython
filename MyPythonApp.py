import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import  GrafickiLikovi as gl
import ast

window = tk.Tk()
def openFileDialog():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    drawPicture(window)
window.title("Draw picture")
menubar = tk.Menu(window)
dropdownmenu = tk.Menu(menubar,tearoff=0)
dropdownmenu.add_command(label ="Open file", command =openFileDialog)
dropdownmenu.add_command(label = "Exit", command = window.quit)
menubar.add_cascade(label ="File", menu= dropdownmenu)

window.config(menu=menubar)
canvas = tk.Canvas(window, bg="white", width= 800,height= 600)
canvas.pack()


def drawPicture():
    file = open(filename, 'r')
    for line in file:
        noenter = line.replace('\n','')
        noenter =noenter.rstrip()
   
        noenter =noenter.split(' ')
        shape= noenter[0]
        boja = noenter[1]
        tocke = noenter[2:]
        tocke =[float(item) for item in tocke]
        funk='gl.'+ shape+'(tocke,"'+boja+'")'
        oblik=eval(funk)
        oblik.Draw(self.canvas)







window.mainloop()