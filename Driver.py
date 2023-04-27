import csv
from multiprocessing.connection import answer_challenge
import random
import numpy as np
import datetime
from FunctionFile import *
from ServerClass import Server
from CustomerClass import Customer
import matplotlib.pyplot as plt

randomDay = random.randint(min(index), max(index))
randomServiceTime = random.randint(min(talk_duration), max(talk_duration))

simulationHours = int(input("How many hours would you like to simulate?"))
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
customerList[0].setServiceStartTime(customerList[0].getEntryTime())
customerList[0].setServiceEndTime(customerList[0].getServiceStartTime() + customerList[0].getServiceTime())
print(customerList[0].toString())


## List of servers
serverList = []
for i in range(serverCount):
    serverList.append(Server(i))

#tick(serverList, customerList, simulationHours*3600, 5, 600)


# Define a dictionary
data = tick(serverList, customerList, simulationHours*3600, 5, 600)

# Extract keys and values from the dictionary
x = list(data.keys())
y = list(data.values())

# Plot the data using Matplotlib
plt.bar(x, y)

# Add labels to the plot
plt.xlabel('Service Time (in seconds)')
plt.ylabel('Frequency')
plt.title('')

# Display the plot
plt.show()





    
