
class Logger:
    def __init__(self, className):
        self.className = className

    def logInfo(self, message):
        print ("[INFO] ", message)
        
    def logError(self, message):
        print ("[ERROR] ", message)