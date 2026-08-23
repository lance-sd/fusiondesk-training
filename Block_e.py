class Ticket:
    def __init__(self,title,status,priority):
        self.title = title
        self.status = status
        self.priority = priority

    def close_ticket(self):
        self.status = "Closed"

    def __str__(self):
        return (f"Title: {self.title}, \n Status: {self.status}, \n Priority: {self.priority}")
    

ticket1 = Ticket("Printer not working", "Open", "High")
ticket1.close_ticket()

print(ticket1)





