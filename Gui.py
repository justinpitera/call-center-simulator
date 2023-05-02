from tkinter import *

def submit():
    totalHours = entryTotalHours.get()
    totalWorkers = entryTotalWorkers.get()
    print(totalHours + " hours")
    print(totalWorkers + " workers")
    

window = Tk()
window.title("Call Center Simulation")

#set window size
WINDOW_LENGTH = 600
WINDOW_WIDTH = 300
window.geometry(str(WINDOW_LENGTH) + "x" + str(WINDOW_WIDTH))
# ----------------------

# Label for text boxes
#lbl1 = Label(window, text = "Enter number of hours: ")
#lbl1.pack(pady = 20, side = LEFT)

#lbl2 = Label(window, text = "Enter number of workers: ")
#lbl2.pack(pady = 40)
# -----------------------

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