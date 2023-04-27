import csv
from multiprocessing.connection import answer_challenge
import datetime
import random
import numpy as np
from CustomerClass import Customer
from ServerClass import Server

servedCustomers = []
abandondedCustomers = []
baulkedCustomers = []
reneggedCustomers = []



## take in time string formatted as 00:00:00 and convert it to total seconds
def toSeconds(time):
    time = str(time)
    numbers = time.split(":")
    hours = int(numbers[0])
    minutes = int(numbers[1])
    seconds = int(numbers[2])
    return hours*3600 + minutes*60 + seconds

def toPercent(percent):
    numberString = percent.split("%")
    number = float(numberString[0]) / 100
    return number

def randomD(min, max):
    return random.uniform(min, max)

def customersTick(customerList):
    for customer in customerList:
        customer.tick()

def tick(serverList, customerList, ticks, max_queue_length, max_waiting_time):
    # make sure there are customers 
    queue = []
    if len(customerList) == 0:
        print("Error: No Customers Specified")
        quit()
    # make sure there are servers 
    if len(serverList) == 0:
        print("There are no servers")
        quit()
    
    # do as many ticks are requested
    for i in range(ticks):
        if len(customerList) != 0:
            if customerList[0].getEntryTime() == i:
                queue.append(customerList[0])
                customerList = customerList[1:]
        # remove baulking customers
        while len(queue) > max_queue_length:
            baulked_cust = queue.pop()
            baulked_cust.setBaulkTime(i)
            print("Customer", str(baulked_cust.id), "baulked from the queue")
            print(baulked_cust.toString(0))

        # remove reneging customers
        for customer in queue:
            if customer.willRenege():
                print("Customer", str(customer.id), "did not want to wait")
                reneggedCustomers.append(customer)
                queue.remove(customer)

        
        # for each server 
        for server in serverList:
            # if they are severing a customer 
            if(server.serving):
                # check if they should have finished with the customer 
                if(server.time >= server.endTime):
                    # They should no longer be serving that customer 
                    server.serving = False
                    print("Server", str(server.id), "finished with Customer", str(server.cust.id), ": ", str(server.cust))
                    servedCustomers.append(server.cust)
                else:
                    # increment the time the server is with the customer 
                    server.tick()
            # if they are not serving a customer 
            else:
                # if there still customers to help
                if(len(queue) != 0):
                    # start serving the next customer 
                    nextCus = queue[0]
                    queue = queue[1:]
                    nextCus.setServiceStartTime(i)
                    nextCus.setServiceEndTime(i + nextCus.getServiceTime())
                    server.serving = True
                    server.newCust(nextCus)
                    print("Server", str(server.id), "is now serving Customer", str(server.cust.id))
        customersTick(queue)

def callsPerDay(hours):
    return int(np.ceil((np.random.poisson(avgCalls) / 8 ) * hours))

def getCustomerCallTimes(hours):
    calls = callsPerDay(hours)
    seconds = hours * 3600
    callTimes = []
    for i in range (0, calls):
        callTimes.append(random.randint(0,seconds))
    callTimes.sort()
    return callTimes

def getCallLengths(callTimes):
    callLengths = []
    totalCallLength = 0
    for i in callTimes:
        length = np.random.poisson(avgLength)
        callLengths.append(length)
        totalCallLength = totalCallLength + length
    print(totalCallLength / 60)
    return callLengths  

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

avgCalls = np.average(incoming_calls)
avgLength=np.average(talk_duration)
avg = sum(abandonded_calls) / len(abandonded_calls)
avgWait = sum(waiting_time) / len(waiting_time)
numofA = len(abandonded_calls)
answerSpeedSecondList = list()
rand = random.randint(0, max(answer_speed))
#print(rand)

def getAvgWait():
    print(avgWait)
    return avgWait