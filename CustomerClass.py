import datetime
import numpy as np

class Customer:
    id = None
    entryTime = None
    serviceTime = None
    serviceStartTime = None
    serviceEndTime = None
    baulkTime = None
    renegTime = None

    def __init__(self, id, entryTime, serviceTime) -> None:
        self.serviceTime = round(serviceTime,2)
        self.id = id
        self.entryTime = round(entryTime,2)
        self.serviceStartTime = 9999999
        self.serviceEndTime = 99999999
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
    
    def getBaulkTime(self):
        return self.baulkTime

    def setBaulkTime(self, baulkTime):
        self.baulkTime = round(baulkTime,2)

    def getRenegTime(self):
        return self.renegTime

    def setRenegTime(self, renegTime):
        self.renegTime = round(renegTime,2)

    def getWaitingTime(self):
        return round(self.serviceStartTime - self.entryTime, 2)

    #def __str__(self) -> str:
    #    return "Customer [id=" + str(self.id) + ", entryTime=" + str(datetime.timedelta(seconds = self.entryTime)) + ", startTime= " + str(datetime.timedelta(seconds = self.serviceStartTime)) + ", serviceTime=" + str(datetime.timedelta(seconds = self.serviceTime)) + ", DepartureTime=" + str(datetime.timedelta(seconds = self.serviceEndTime)) + ", baulkTime=" + str(datetime.timedelta(seconds = self.baulkTime)) + ", renegTime=" + str(datetime.timedelta(seconds = self.renegTime)) + "]"
    
    #def toString(self):
    #            return "Customer [id=" + str(self.id) + ", entryTime=" + str(datetime.timedelta(seconds = self.entryTime)) + ", startTime= " + str(datetime.timedelta(seconds = self.serviceStartTime)) + ", serviceTime=" + str(datetime.timedelta(seconds = self.serviceTime)) + ", DepartureTime=" + str(datetime.timedelta(seconds = self.serviceEndTime)) + ", baulkTime=" + str(datetime.timedelta(seconds = self.baulkTime)) + ", renegTime=" + str(datetime.timedelta(seconds = self.renegTime)) + "]"
    def __str__(self) -> str:
        return "Customer [id=" + str(self.id) + ", entryTime=" + str(datetime.timedelta(seconds = self.entryTime)) + ", startTime= " + str(datetime.timedelta(seconds = self.serviceStartTime)) + ", serviceTime=" + str(datetime.timedelta(seconds = self.serviceTime)) + ", DepartureTime=" + str(datetime.timedelta(seconds = self.serviceEndTime)) +  "]"
    
    def toString(self):
                return "Customer [id=" + str(self.id) + ", entryTime=" + str(datetime.timedelta(seconds = self.entryTime)) + ", startTime= " + str(datetime.timedelta(seconds = self.serviceStartTime)) + ", serviceTime=" + str(datetime.timedelta(seconds = self.serviceTime)) + ", DepartureTime=" + str(datetime.timedelta(seconds = self.serviceEndTime)) +  "]"

    def toString(self, baulkReneg):
        if baulkReneg == 0:
            return "Customer [id=" + str(self.id) + ", entryTime=" + str(datetime.timedelta(seconds = self.entryTime)) + ", baulkTime=" + str(datetime.timedelta(seconds = self.baulkTime)) +  "]"
        if baulkReneg == 1:
            return "Customer [id=" + str(self.id) + ", entryTime=" + str(datetime.timedelta(seconds = self.entryTime)) + ", renegTime=" + str(datetime.timedelta(seconds = self.renegTime)) +  "]"
        else:
            return "Customer [id=" + str(self.id) + ", entryTime=" + str(datetime.timedelta(seconds = self.entryTime)) + ", startTime= " + str(datetime.timedelta(seconds = self.serviceStartTime)) + ", serviceTime=" + str(datetime.timedelta(seconds = self.serviceTime)) + ", DepartureTime=" + str(datetime.timedelta(seconds = self.serviceEndTime)) +  "]"
