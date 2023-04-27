import csv
from multiprocessing.connection import answer_challenge
import random
from ServerClass import Server
from CustomerClass import Customer
from FunctionFile import *

index = []
incoming_calls = []
answer_calls = []
answer_rate = []
abandonded_calls = []
answer_speed = []
talk_duration = []
waiting_time =[]
service_level = []


#  CSV FORMAT
#  Index,Incoming Calls,Answered Calls,Answer Rate,Abandoned Calls,Answer Speed (AVG),Talk Duration (AVG),Waiting Time (AVG),Service Level (20 Seconds)
#  Open sample data file
with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    #next(reader)

    for row in reader:
        index.append(int(row[0]))
        incoming_calls.append(int(row[1]))
        answer_calls.append(int(row[2]))
        answer_rate.append(str(row[3]))
        abandonded_calls.append(int(row[4]))
        answer_speed.append(toSeconds(row[5]))
        talk_duration.append(toSeconds(row[6]))
        waiting_time.append(toSeconds(row[7]))
        service_level.append(str(row[8]))

avgWaitTime = sum(waiting_time) / len(waiting_time)
randomServiceTime = random.randint(min(talk_duration), max(talk_duration))

customerCount = int(input("how many customers for this simulation: "))
serverCount = int(input("how many servers for this simulation: "))

#intialize total num of customer
customerEntered = 0.0
customerList = []
for i in range(customerCount):
    num = random.randint(0, 4)
    if num == 4:
        cus = Customer(i, randomD(0.2, 1.3) + customerEntered, random.randint(0, randomServiceTime + 2), avgWaitTime)
    else:
        cus = Customer(i, randomD(0.2, 1.3) + customerEntered, random.randint(0, randomServiceTime), avgWaitTime)
    customerEntered = cus.getEntryTime()
    customerList.append(cus)
customerList[0].setServiceStartTime(customerList[0].getEntryTime())
customerList[0].setServiceEndTime(customerList[0].getServiceStartTime() + customerList[0].getServiceTime())
print(customerList[0].toString())

for i in range(1, len(customerList)):
    cus = customerList[i]
    prevCus = customerList[i-1]

    cus.setServiceStartTime(prevCus.getServiceEndTime())
    cus.setServiceEndTime(cus.getServiceStartTime() + cus.getServiceTime())
    print(cus.toString())

## List of servers
serverList = []
for i in range(serverCount):
    serverList.append(Server(i))

## servers store the customer as a field
for server in serverList:
    if(len(customerList) != 0):
        customer = customerList.pop(0)
        customer.beingServed = True
        server.newCust(customer)
        server.serving = True
        print("Server", str(server.id), "is now serving Customer", str(server.cust.id))

tick(serverList, customerList, 3600, avgWaitTime)

