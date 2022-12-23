import datetime

class Event:
    user = str
    machine = str
    date = datetime.datetime
    type = str
    
    def __init__(self, user, machine, date, type):
        self.user = user
        self.machine = machine
        self.date = date
        self.type = type
        
    
