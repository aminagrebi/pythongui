'''
Dec 25,  2017
Recipe:  B04829_01_03
@author: Amin Agrebi
'''
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")

# Disable resizing the GUI
#win.resizable(0,0)    

# Adding a Label
ttk.Label(win, text="A Label").grid(column=0, row=0) 

#======================
# Start GUI
#======================
win.mainloop()