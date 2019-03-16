from tkinter import Tk,Frame,Grid, Label, Button, Canvas
from rbgSensor import getRGB

app = Tk()
app.title("RGB GUI") # * Name of the window 

# * Main frame on which everything is added 
f = Frame(app,width=800,height=500)
f.grid(row=1,column=0,sticky="NW")
f.grid_propagate(0)
f.update()

# * Title Label 
title = Label(f,text="RGB Viewer")
title.config(font=("Roboto Slab", 20))
title.place(x=400, y=50, anchor="center")

colors=getRGB()

red=Label(f,text="RED: "+str(colors[0]))
red.config(font=("Roboto Slab", 15))
red.place(x=400, y=100, anchor="center")

green=Label(f,text="GREEN: "+str(colors[1]))
green.config(font=("Roboto Slab", 15))
green.place(x=400, y=150, anchor="center")

blue=Label(f,text="BLUE: "+str(colors[2]))
blue.config(font=("Roboto Slab", 15))
blue.place(x=400, y=200, anchor="center")

colorLabel=Label(f,text=colors[3])
colorLabel.config(font=("Roboto Slab", 15))
colorLabel.place(x=400, y=250, anchor="center")

def make():
    colors=getRGB()
    red.config(text="RED: "+str(colors[0]))
    green.config(text="GREEN: "+str(colors[1]))
    blue.config(text="BLUE: "+str(colors[2]))
    colorLabel.config(text=colors[3])
    app.after(1000,make)

make()

app.mainloop()