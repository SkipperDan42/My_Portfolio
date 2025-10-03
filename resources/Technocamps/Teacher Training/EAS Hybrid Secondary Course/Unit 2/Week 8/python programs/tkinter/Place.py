import tkinter as tk



colours = ['red','green','orange','white','yellow','blue']



x=0

y=0


for c in colours:

    l=tk.Label(text=c, relief=tk.RIDGE, width=15)

    l.place(x=x,y=y,width=125,height=25)

    
    e=tk.Entry(bg=c, relief=tk.SUNKEN, width=10)

    e.place(x=x+125, y=y,width=125,height=25)

    
    y=y+25



tk.mainloop()




