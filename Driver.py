import csv
from locale import currency
from multiprocessing.connection import answer_challenge
import random
import numpy as np
import datetime
from FunctionFile import *
from ServerClass import Server
from CustomerClass import Customer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def main(totalHours, totalServers) -> dict:

    simulationHours = int(totalHours)
    simulationTime = simulationHours * 3600
    
    serverCount = int(totalServers)
    callTimes = getCustomerCallTimes(simulationHours)
    callLengths = getCallLengths(callTimes)

    customerList = []

    for i in range(len(callTimes)):
        cus = Customer(i, callTimes[i], callLengths[i], getAvgWait())
        customerList.append(cus)

    ## List of servers
    serverList = []
    for i in range(serverCount):
        serverList.append(Server(i))

    simulationData = simulate(serverList, customerList, simulationTime, 5)

    callsLabel.config(text="Total Calls: " + str(len(callTimes)) )
    servedLabel.config(text="Total Customers Served: " + str(len(getServedCustomers())))
    baulkedLabel.config(text="Total Customers Baulked: " + str(len(getBaulkedCustomers())))
    renegeLabel.config(text="Total Customers Renegged: " + str(len(getReneggedCustomers())))
    cusInQueueLabel.config(text="Customers still in queue and/or currently being served: " + str((len(callTimes) - (len(getServedCustomers()) + len(getBaulkedCustomers()) + len(getReneggedCustomers())))))
    
    return simulationData

from tkinter import *

def submit():
    currentData = dict
    totalHours = entryTotalHours.get()
    totalWorkers = entryTotalWorkers.get()

    currentData = main(totalHours, totalWorkers)

    # create a new window
    graphWindow = Toplevel(window)
    graphWindow.title("Customer Service Time Plot")

    # create a figure object
    fig = plt.figure(figsize=(6, 4), dpi=100)

    # create a subplot
    ax = fig.add_subplot(111)

    # plot the data using the same code as in the main function
    x = list(currentData.keys())
    y = list(currentData.values())
    ax.bar(x, y)

    # Add labels to the plot
    ax.set_xlabel('Service Time (in seconds)')
    ax.set_ylabel('Probability of Service Time')
    ax.set_title('Distribution of Service Times')

    # create a canvas to display the plot
    canvas = FigureCanvasTkAgg(fig, master=graphWindow)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # display the window
    #graphWindow.mainloop()


window = Tk()
window.title("Call Center Simulation")

#set window size
WINDOW_LENGTH = 800
WINDOW_WIDTH = 300
window.geometry(str(WINDOW_LENGTH) + "x" + str(WINDOW_WIDTH))
# ----------------------

# Label for text boxes
lbl1 = Label(window, text = "Enter number of hours: ")
lbl1.grid(row = 0, column= 0, sticky=W, pady=2)

lbl2 = Label(window, text = "Enter number of workers: ")
lbl2.grid(row= 1, column=0, sticky=W, pady=2)
# -----------------------

# Text Boxes for input

# Text Box for Hours
entryTotalHours = Entry()
entryTotalHours.config(font=('Arial',12))
entryTotalHours.insert(0, "")
entryTotalHours.config(width=15)

# Text boc for Servers
entryTotalWorkers = Entry()
entryTotalWorkers.config(font=('Arial',12))
entryTotalWorkers.insert(0, "")
entryTotalWorkers.config(width=15)

# Text box locations
entryTotalHours.grid(row = 0, column=2, sticky=W, pady= 2)
entryTotalWorkers.grid(row = 1, column= 2, sticky=W, pady= 2)
# ------------------------

# Submit button
run = Button(window,text="Run Simulation",command=submit)
run.grid(row=2, column=1, sticky= W)
# ------------------------

# Output Labels
callsLabel = Label(window, text="")
callsLabel.grid(row=3, column=0, pady= 2, sticky=W)

servedLabel = Label(window, text="")
servedLabel.grid(row=4, column=0, pady= 2, sticky=W)

baulkedLabel = Label(window, text="")
baulkedLabel.grid(row=5, column=0, pady= 2, sticky=W)

renegeLabel = Label(window, text="")
renegeLabel.grid(row=6, column=0, pady= 2, sticky=W)

cusInQueueLabel = Label(window, text="")
cusInQueueLabel.grid(row=7, column=0, pady= 2, sticky=W)
# ------------------------





window.mainloop()