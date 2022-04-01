# import modules
from tkinter import *
from time import strftime

root = Tk()
root.title('Digital Computer Clock')  # adds title to tkinter window


# function used to display time on window
def time():
    string = strftime("%H:%M:%S %p")
    lbl.config(text=string)
    lbl.after(1000, time)


# styling the label widget which displays the clock
lbl = Label(root, font = "arial 160 bold", bg="white", fg="black")

# pack the method in tkinter packs widgets into rows or columns. Positionss label
lbl.pack(anchor="center", fill="both", expand=1)

time()  # time function is called
mainloop()  # runs the application program
