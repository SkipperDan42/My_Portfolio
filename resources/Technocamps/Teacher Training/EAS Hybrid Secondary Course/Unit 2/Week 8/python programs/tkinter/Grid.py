import tkinter as tk



colours = ['red','green','orange','white','yellow','blue'] 

row = 0 

for c in colours: 

    tk.Label(text=c, relief=tk.RIDGE, width=15).grid(row=row,column=0)

    tk.Entry(bg=c, relief=tk.SUNKEN, width=10).grid(row=row,column=1)         

    row = row + 1 



tk.mainloop


