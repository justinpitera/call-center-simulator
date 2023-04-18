from CustomerClass import Customer
class Server:
    serving = False
    time = 0.0
    cust = Customer
    def __init__(self) -> None:
        pass

    def newCust(self, customer):
        self.cust = customer
        self.time = customer.getEntryTime()
    
    def tick(self):
        self.time += 1
        
