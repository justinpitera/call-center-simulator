from CustomerClass import Customer
class Server:
    ## Constructor 
    def __init__(self, id) -> None:
        self.id = id
        self.cust = None
        self.endTime = 0.0
        self.time = 0.0
        self.serving = False

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
        
