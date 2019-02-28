from tkinter import Tk,Frame,Grid, Label, Button, Canvas
from rbgSensor import getRGB

app = Tk()
app.title("RGB GUI") # * Name of the window 

# * Main frame on which everything is added 
f = Frame(app,width=800,height=500)
f.grid(row=1,column=0,sticky="NW")
f.grid_propagate(0)
f.update()

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

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

canvas=Canvas(f,width=200,height=200)
canvas.place(x=400, y=250, anchor="center")
canvas.create_rectangle(50, 25, 150, 75, fill=_from_rgb((colors[0],colors[1],colors[2])))

def make():
    colors=getRGB()
    red.config(text="RED: "+str(colors[0]))
    green.config(text="GREEN: "+str(colors[1]))
    blue.config(text="BLUE: "+str(colors[2]))
    canvas.create_rectangle(50, 25, 150, 75, fill=_from_rgb((colors[0],colors[1],colors[2])))
    app.after(1000,make)

make()

app.mainloop()