import random
import numpy as np
###
 # Customer Class with ID, entryTime, and ServiceTime
 # 
 # @author Matthew Tobino, Andy Pham, Justin Pitera, Sean Pandolfo
 ##
class Customer:
    id = None
    entryTime = None
    serviceTime = None
    serviceStartTime = None
    serviceEndTime = None
    waitingTime = None
    maxWaitingTime = None
    beingServed = False

    def __init__(self, id, entryTime, serviceTime, avgWait) -> None:
        self.serviceTime = round(serviceTime,2)
        self.id = id
        self.entryTime = round(entryTime,2)
        # Renege variables 
        self.waitingTime = self.entryTime
        self.maxWaitingTime = np.random.poisson(avgWait)
        pass
    
    def getId(self):
        return self.id
    
    def getEntryTime(self):
        return self.entryTime
    
    def getServiceTime(self):
        return self.serviceTime
    
    def getServiceStartTime(self):
        return self.serviceStartTime
    
    def getServiceEndTime(self):
        return self.serviceEndTime

    def setServiceStartTime(self, startTime):
        self.serviceStartTime = round(startTime,2)
    
    def setServiceEndTime(self, endTime):
        self.serviceEndTime = round(endTime,2)

    # for renege 
    def tick(self):
        self.waitingTime += 1

    # renege check
    def willRenege(self):
        if(self.waitingTime >= self.maxWaitingTime):
            return True
        return False

    def __str__(self) -> str:
        return "Customer [id=" + str(self.id) + ", entryTime=" + str(self.entryTime) + ", startTime= " + str(self.serviceStartTime) + ", serviceTime=" + str(self.serviceTime) + ", DepartureTime=" + str(self.serviceEndTime) + "]"
    
    def toString(self):
        return "Customer [id=" + str(self.id) + ", entryTime=" + str(self.entryTime) + ", startTime= " + str(self.serviceStartTime) + ", serviceTime=" + str(self.serviceTime) + ", DepartureTime=" + str(self.serviceEndTime) + "]"
