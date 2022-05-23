from tkinter import *
root = Tk()
#create Label Widget
myLabel1 = Label(root, text="Hello world")
myLabel2 = Label(root, text="CS is cool!!")
#myLabel1 = Label(root, text="Hello world").grid(row=0, column=0)
#myLabel2 = Label(root, text="CS is cool!!").grid(row=1, column=1)
#pack onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
root.mainloop()

