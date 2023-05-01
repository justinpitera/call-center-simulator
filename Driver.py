import csv
from multiprocessing.connection import answer_challenge
import random
import numpy as np
import datetime
from FunctionFile import *
from ServerClass import Server
from CustomerClass import Customer

randomDay = random.randint(min(index), max(index))
randomServiceTime = random.randint(min(talk_duration), max(talk_duration))

simulationHours = int(input("How many hours would you like to simulate?"))
simulationTime = simulationHours * 3600
customerCount = callsPerDay(simulationHours)
#customerCount = int(input("how many customers for this simulation: "))
serverCount = int(input("how many servers for this simulation: "))
callTimes = getCustomerCallTimes(simulationHours)
callLengths = getCallLengths(callTimes)


#intialize total num of customer
customerEntered = 0.0
customerList = []

for i in range(len(callTimes)):
    cus = Customer(i, callTimes[i], callLengths[i], getAvgWait())
    customerList.append(cus)


## List of servers
serverList = []
for i in range(serverCount):
    serverList.append(Server(i))

simulate(serverList, customerList, simulationTime, 5)
print("Total Calls: ", len(callTimes))
print("Total Customers Served: ", len(getServedCustomers()))
print("Total Customers Baulked: ", len(getBaulkedCustomers()))
print("Total Customers Renegged: ", len(getReneggedCustomers()))
print("Customers still in queue and/or currently being served: ", (len(callTimes) - (len(getServedCustomers()) + len(getBaulkedCustomers()) + len(getReneggedCustomers()))))
    
