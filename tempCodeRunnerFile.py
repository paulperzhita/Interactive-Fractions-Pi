from tkinter import *

app = Tk()
app.title("Interactive Fractions")
f = Frame(app,width=500,height=500)
f.grid(row=1,column=0,sticky="NW")
f.grid_propagate(0)
f.update()
title = Label(f,text="Welcome To Interactive Fractions")
title.config(font=("Roboto Slab", 20))
title.place(x=250, y=50, anchor="center")
question = Label(f,text="Question comes here")
question.config(font=("Roboto Slab", 15))
question.place(x=250, y=100, anchor="center")
submit=Button(f,text="Submit")
submit.config(font=("Roboto Slab", 60))
submit.place(x=250, y=200, anchor="center")
app.mainloop()