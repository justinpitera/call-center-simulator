import random
from CustomerClass import Customer
from ServerClass import Server

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


def tick(serverList, customerList, ticks, avgWait):
    # make sure there are customers 
    if len(customerList) == 0:
        print("No customers in the queue")
        quit()
    # make sure there are servers 
    if len(serverList) == 0:
        print("There are no servers")
        quit()
    
    # do as many ticks are requested
    for i in range(ticks):
        
        for customer in customerList:
            if customer.willRenege():
                print("Customer", str(customer.id), "did not want to wait", str(customer.maxWaitingTime), "seconds")
                customerList.remove(customer)
        
        # for each server 
        for server in serverList:
            # if they are severing a customer 
            if(server.serving):
                # check if they should have finished with the customer 
                if(server.time >= server.endTime):
                    # They should no longer be serving that customer 
                    server.serving = False
                    print("Server", str(server.id), "finished with Customer", str(server.cust.id))
                else:
                    # increment the time the server is with the customer 
                    server.tick()
            # if they are no serving a customer 
            else:
                # if there still customers to help
                if(len(customerList) != 0):
                    # start serving the next customer 
                    server.serving = True
                    customer = customerList.pop(0)
                    server.newCust(customer)
                    print("Server", str(server.id), "is now serving Customer", str(server.cust.id))
        customersTick(customerList)