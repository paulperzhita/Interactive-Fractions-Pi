from tkinter import Tk,Frame,Grid, Label, Button
from rbgSensor import getRGB

app = Tk()
app.title("RGB GUI") # * Name of the window 

# * Main frame on which everything is added 
f = Frame(app,width=800,height=500)
f.grid(row=1,column=0,sticky="NW")
f.grid_propagate(0)
f.update()

def make():
    # * Title Label 
    title = Label(f,text="RGB Viewer")
    title.config(font=("Roboto Slab", 20))
    title.place(x=400, y=50, anchor="center")

    colors=getRGB()

    red=Label(f,text="RED: "+str(colors[0]))
    red.config(font=("Roboto Slab", 15))
    red.place(x=400, y=100, anchor="center")

    green=Label(f,text="Green: "+str(colors[1]))
    green.config(font=("Roboto Slab", 15))
    green.place(x=400, y=150, anchor="center")

    blue=Label(f,text="BLUE: "+str(colors[2]))
    blue.config(font=("Roboto Slab", 15))
    blue.place(x=400, y=200, anchor="center")

    app.after(1000,make)

make()

app.mainloop()