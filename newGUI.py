from tkinter import Tk,Frame,Grid, Label, Button

app = Tk()
app.title("Interactive Fractions") # * Name of the window 

# * Main frame on which everything is added 
f = Frame(app,width=800,height=500)
f.grid(row=1,column=0,sticky="NW")
f.grid_propagate(0)
f.update()

# * Title Label 
title = Label(f,text="Welcome To Interactive Fractions")
title.config(font=("Roboto Slab", 20))
title.place(x=400, y=50, anchor="center")

# * Question Label
question = Label(f,text="Question comes here")
question.config(font=("Roboto Slab", 15))
question.place(x=400, y=100, anchor="center")

# * Submit Button
submit=Button(f,text="Submit")
submit.config(font=("Roboto Slab", 60))
submit.place(x=400, y=220, anchor="center")

# * Hint Label
hint = Label(f,text="Hint comes here")
hint.config(font=("Roboto Slab", 15))
hint.place(x=400, y=360, anchor="center")

app.mainloop() # * Starts the GUI