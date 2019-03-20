import datetime

class Logger:
    def __init__(self):
        self.messages = []
        
    def log(self, msg):
        self.messages.append((datetime.datetime.now(), msg))