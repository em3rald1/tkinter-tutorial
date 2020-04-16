import tkinter
from tkinter import *
from tkinter import ttk #there will be cool buttons
from tkinter.ttk import *
from tkinter import filedialog
import subprocess

def Quit(ev):
   global root
   root.destroy()

def Browse(ev):
   global fn
   fn = filedialog.Open(root, filetypes=[("*.txt files", ".txt")]).show()
   if(fn == ''):
     return

def Open(ev):
   subprocess.run(fn)

root = Tk()
root.title("Programm 1")
root.iconbitmap("path/to/file")

btn = Button(root, text = "Quit")
btn.bind("<Button-1>", Quit)
btn2 = Button(root, text = "Browse")
btn2.bind("<Button-1>", Browse)
btn3 = Button(root, text = "Open")
btn3.bind("<Button-1>", Quit)

btn.place(x = 10, y = 10, height = 20, width = 30)
btn2.place(x = 60, y = 10, height = 20, width = 30)
btn3.place(x = 110, y = 10, height = 20, width = 30)

root.mainloop()
