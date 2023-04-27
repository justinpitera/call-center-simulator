from CustomerClass import Customer
class Server:
    serving = False
    time = 0.0
    endTime = 0.0
    cust = None
    id = 0
    ## Constructor 
    def __init__(self, id) -> None:
        self.id = id
        pass
    ## Add the customer to the 
    def newCust(self, customer):
        self.cust = customer
        self.time = customer.getServiceStartTime()
        self.endTime = customer.getServiceEndTime()
    
    def tick(self):
        self.time += 1
    
    def __str__(self) -> str:
        return "Server " + str(self.id) + " Serving:" + str(self.serving) + " Current time: " + str(self.time)
        
