import csv
from multiprocessing.connection import answer_challenge
import random
import numpy as np
import datetime
from FunctionFile import *
from ServerClass import Server
from CustomerClass import Customer

def main(totalHours, totalServers):
    #randomDay = random.randint(min(index), max(index))
    #randomServiceTime = random.randint(min(talk_duration), max(talk_duration))

    simulationHours = int(totalHours)
    simulationTime = simulationHours * 3600
    customerCount = callsPerDay(simulationHours)
    #customerCount = int(input("how many customers for this simulation: "))
    serverCount = int(totalServers)
    callTimes = getCustomerCallTimes(simulationHours)
    callLengths = getCallLengths(callTimes)


    #intialize total num of customer
    #customerEntered = 0.0
    customerList = []

    for i in range(len(callTimes)):
        cus = Customer(i, callTimes[i], callLengths[i], getAvgWait())
        customerList.append(cus)


    #tick(serverList, customerList, timeToRun, avgWaitTime)


    ## List of servers
    serverList = []
    for i in range(serverCount):
        serverList.append(Server(i))

    simulate(serverList, customerList, simulationTime, 5)
    callsLabel.config(text="Total Calls: " + str(len(callTimes)) )
    servedLabel.config(text="Total Customers Served: " + str(len(getServedCustomers())))
    baulkedLabel.config(text="Total Customers Baulked: " + str(len(getBaulkedCustomers())))
    renegeLabel.config(text="Total Customers Renegged: " + str(len(getReneggedCustomers())))
    cusInQueueLabel.config(text="Customers still in queue and/or currently being served: " + str((len(callTimes) - (len(getServedCustomers()) + len(getBaulkedCustomers()) + len(getReneggedCustomers())))))
    
    
    print("Total Calls: ", len(callTimes))
    print("Total Customers Served: ", len(getServedCustomers()))
    print("Total Customers Baulked: ", len(getBaulkedCustomers()))
    print("Total Customers Renegged: ", len(getReneggedCustomers()))
    print("Customers still in queue and/or currently being served: ", (len(callTimes) - (len(getServedCustomers()) + len(getBaulkedCustomers()) + len(getReneggedCustomers()))))

from tkinter import *

def submit():
    totalHours = entryTotalHours.get()
    totalWorkers = entryTotalWorkers.get()
    main(totalHours, totalWorkers)
    

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
callsLabel = Label(window, text="", font=('Arial',12))
callsLabel.grid(row=3, column=0, pady= 2, sticky=W)

servedLabel = Label(window, text="", font=('Arial',12))
servedLabel.grid(row=4, column=0, pady= 2, sticky=W)

baulkedLabel = Label(window, text="", font=('Arial',12))
baulkedLabel.grid(row=5, column=0, pady= 2, sticky=W)

renegeLabel = Label(window, text="", font=('Arial',12))
renegeLabel.grid(row=6, column=0, pady= 2, sticky=W)

cusInQueueLabel = Label(window, text="", font=('Arial',12))
cusInQueueLabel.grid(row=7, column=0, pady= 2, sticky=W)
# ------------------------


window.mainloop()

