class event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.num = 0
        
    def add_participant(self):
        self.num +=1
        
    def participant_count(self):
        return self.num
    
event1 = event("Terry","12/09/2024")
event1.add_participant()

print(event1.participant_count())