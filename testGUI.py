from tkinter import *

# if you are still working under a Python 2 version, 
# comment out the previous line and uncomment the following line

root = Tk()
root.configure(width=600,height=400)
root.title("Hello")
frame= Frame(root,bg="red",width=600,height=400)
frame.place(x=20, y=0)
label = Label(frame, text="Welcome to Interactive Fractions")
label.config(font=("Courier", 20))
label.pack()
# frame.pack_propagate(False) 
# w = .Label(root, text="Hello Tkinter!")
# w.pack()

root.mainloop() 