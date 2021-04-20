#Write a class Train which has methods to book a ticket, get status(no of seats), 
# and get fare information of trains running under Indian Railways.

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("*************")
        print(f"Name of the train is {self.name}")
        print(f"Seats available are {self.seats}")
        print("*************")

    def fareInfo(self):
        print(f"Price of the ticket is Rs.{self.fare}") 

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticked has been booked. Your seat number is {self.seats}")
            self.seats = self.seats -1
        else:
            print("No seats available")

    def cancelTicket(self, seatNo):
        pass

intercity = Train("Intercity Express: 1077", 190, 2)
intercity.getStatus()
# intercity.fareInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()