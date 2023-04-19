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
        self.baulkTime = None
        self.renegTime = None
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

    def __str__(self) -> str:
        return "Customer [id=" + str(self.id) + ", entryTime=" + str(self.entryTime) + ", startTime= " + str(self.serviceStartTime) + ", serviceTime=" + str(self.serviceTime) + ", DepartureTime=" + str(self.serviceEndTime) + ", baulkTime=" + str(self.baulkTime) + ", renegTime=" + str(self.renegTime) + "]"
    
    def toString(self):
        return "Customer [id=" + str(self.id) + ", entryTime=" + str(self.entryTime) + ", startTime= " + str(self.serviceStartTime) + ", serviceTime=" + str(self.serviceTime) + ", DepartureTime=" + str(self.serviceEndTime) + ", baulkTime=" + str(self.baulkTime) + ", renegTime=" + str(self.renegTime) + "]"
