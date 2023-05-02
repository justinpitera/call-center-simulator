from tkinter import *


def submit():
    totalHours = entryTotalHours.get()
    totalWorkers = entryTotalWorkers.get()
    print(totalHours + " hours")
    print(totalWorkers + " workers")

    # Opens a new window for other data
    newWindow = Toplevel(window)
    newWindow.title("New Window")
    newWindow.geometry("600x600")
    Label(newWindow, text ="This is a new window").pack()


    

window = Tk()
window.title("Call Center Simulation")

#set window size
WINDOW_LENGTH = 600
WINDOW_WIDTH = 300
window.geometry(str(WINDOW_LENGTH) + "x" + str(WINDOW_WIDTH))
# ----------------------
    
# Text Boxes for input
entryTotalHours = Entry()
entryTotalHours.config(font=('Arial',15))
entryTotalHours.insert(0, "Total Hours")
entryTotalHours.config(width=15)


entryTotalWorkers = Entry()
entryTotalWorkers.config(font=('Arial',15))
entryTotalWorkers.insert(0, "Total Workers")
entryTotalWorkers.config(width=15)



entryTotalHours.pack(pady = 20)
entryTotalWorkers.pack(pady = 40)
# ------------------------

# Submit button
submit = Button(window,text="submit",command=submit)
submit.pack(side = BOTTOM)
# ------------------------

window.mainloop()