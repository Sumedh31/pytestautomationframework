import os


class Util():
    def __init__(self):
        #self.CurrentWorkingDirectory=os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir))
        self.CurrentWorkingDirectory = os.getcwd()
        
    def GetHomeDirectory(self):
        if "Lib" not in self.CurrentWorkingDirectory:
            LWCD=self.CurrentWorkingDirectory.split("Testscripts")
        else:
            LWCD=self.CurrentWorkingDirectory.split("Lib")
        return LWCD[0]
    
        