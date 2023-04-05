
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
        self.serviceTime = serviceTime
        self.id = id
        self.entryTime = entryTime
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

    def setStartTime(self, startTime):
        self.serviceStartTime = startTime
    
    def setServiceEndTime(self, endTime):
        self.serviceEndTime = endTime

    