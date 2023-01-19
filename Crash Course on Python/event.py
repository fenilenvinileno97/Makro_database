"""This script is made for reporting the current users that are connected and machines which are being used"""

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
        
def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key = get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, user in machines.items():
        if len(user) > 0:
            user_list = ", ".join(user)
            return "{}: {}".format(machine, user_list)
        
events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]
 
users = current_users(events)
print(users)      
