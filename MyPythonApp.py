import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import  GrafickiLikovi as gl

window = tk.Tk()
def openFileDialog():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
window.title("Draw picture")
menubar = tk.Menu(window)
dropdownmenu = tk.Menu(menubar,tearoff=0)
dropdownmenu.add_command(label ="Open file", command =openFileDialog)
dropdownmenu.add_command(label = "Exit", command = window.quit)
menubar.add_cascade(label ="File", menu= dropdownmenu)

window.config(menu=menubar)
canvas = tk.Canvas(window, bg="white", width= 800,height= 600)
canvas.pack()
tocke=[0, 0, 200, 100]
linija = gl.Line(tocke, "red")
linija.Draw(canvas)



window.mainloop()