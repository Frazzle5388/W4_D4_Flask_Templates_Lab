from models.event import *

event1 = Event("01/01/2022", "Beautiful Babies Contest", 100,"pretty babies")
event2 = Event("02/01/2022", "Food Tasting Festival", 75, "Tasting great recipes")
event3 = Event("03/01/2022", "Model Plane Airshow", 99, "Model plane enthusiasts")
event4 = Event("05/01/2022", "Gym Open Day", 25, "Recruitment Drive")
events = [event1, event2, event3, event4]

def add_new_event(event):
    events.append(event)