import random
import numpy as np
import datetime
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
    baulkTime = None
    renegTime = None

    def __init__(self, id, entryTime, serviceTime, avgWait) -> None:
        self.serviceTime = round(serviceTime,2)
        self.id = id
        self.entryTime = round(entryTime,2)
        # Renege variables 
        self.waitingTime = 0
        self.maxWaitingTime = np.random.poisson(avgWait)
        self.serviceStartTime = 0
        self.serviceEndTime = 0
        self.baulkTime = 0
        self.renegTime = 0
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

    def setBaulkTime(self):
        self.baulkTime = self.entryTime + self.waitingTime
    
    def setRenegTime(self):
        self.renegTime = self.entryTime + self.waitingTime

    def removeMaxWaitingTime(self):
        self.maxWaitingTime = 99999999999999999

    # for renege 
    def tick(self):
        self.waitingTime += 1

    # renege check
    def willRenege(self):
        if(self.waitingTime >= self.maxWaitingTime):
            return True
        return False

    def __str__(self) -> str:
         return "Customer [id=" + str(self.id) + ", entryTime=" + str(datetime.timedelta(seconds = self.entryTime)) + ", startTime= " + str(datetime.timedelta(seconds = self.serviceStartTime)) + ", serviceTime=" + str(datetime.timedelta(seconds = self.serviceTime)) + ", DepartureTime=" + str(datetime.timedelta(seconds = self.serviceEndTime)) + "]"
    
    def printRenegged(self):
        return "Customer [id=" + str(self.id) + ", entryTime=" + str(datetime.timedelta(seconds = self.entryTime)) + ", renegTime=" + str(datetime.timedelta(seconds = self.renegTime)) + "]"

    def printBaulk(self):
        return "Customer [id=" + str(self.id) + ", entryTime=" + str(datetime.timedelta(seconds = self.entryTime)) + ", baulkTime=" + str(datetime.timedelta(seconds = self.baulkTime)) +  "]"

    def toString(self):
         return "Customer [id=" + str(self.id) + ", entryTime=" + str(datetime.timedelta(seconds = self.entryTime)) + ", startTime= " + str(datetime.timedelta(seconds = self.serviceStartTime)) + ", serviceTime=" + str(datetime.timedelta(seconds = self.serviceTime)) + ", DepartureTime=" + str(datetime.timedelta(seconds = self.serviceEndTime)) +  "]"