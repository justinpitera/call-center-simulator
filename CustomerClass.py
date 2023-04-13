
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

    def __init__(self, id, entryTime, serviceTime) -> None:
        self.serviceTime = round(serviceTime,2)
        self.id = id
        self.entryTime = round(entryTime,2)
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

    def toString(self):
        return "Customer [id=" + str(self.id) + ", entryTime=" + str(self.entryTime) + ", startTime= " + str(self.serviceStartTime) + ", serviceTime=" + str(self.serviceTime) + ", DepartureTime=" + str(self.serviceEndTime) + "]"
