'''
Created on 01-Apr-2019

@author: Sumedh.Tambe
'''
import  time
#import ConfigReader
import Lib


 
 
 
class Logger():
    
    def __init__(self,LOG_LEVEL):
        
        self.LOG_LEVEL = LOG_LEVEL
        self.dict = {'DEBUG': 2, 'INFO': 1, 'ERROR': 0}
        
        objUTIL = Lib.Utils.Util()
        self.PWorkingDirectory = objUTIL.GetHomeDirectory()
        print(self.PWorkingDirectory)
#         CONFIG = ConfigReader.Configuration(self.PWD+"Config\DITConfig.ini")
#         LOG_LEVEL = CONFIG.ENV.LOG_LEVEL      
    def Debug(self,msg):
        targetfile=open(self.PWorkingDirectory+'Log\Log.log','a')
        if(self.dict(self.LOG_LEVEL.upper()>=2)):
            print(time.strftime("%d/%m/%Y %I:%M:%S %p")+"DEBUG"+str(msg))
            targetfile.write(time.strftime("%d/%m/%Y %I:%M:%S %p")+"DEBUG:"+str(msg))
            targetfile.write("\n")
            targetfile.close()
    def Info(self, msg):
        target = open(self.PWorkingDirectory + 'Log\log1.log', 'a')
        if self.dict[self.LOG_LEVEL.upper()] >= 1:
            print (time.strftime("%d/%m/%Y %I:%M:%S %p") + " INFO: " + (str(msg)))
            target.write(time.strftime("%d/%m/%Y %I:%M:%S %p") + " Info: " + (str(msg)))
            target.write('\n')
            target.close()                 
 
 
    def Error(self, msg):
        target = open(self.PWorkingDirectory + 'Log\log1.log', 'a')
        if self.dict[self.LOG_LEVEL.upper()] > 0:
            print (time.strftime("%d/%m/%Y %I:%M:%S %p") + " ERROR: " + (str(msg)))
            target.write(time.strftime("%d/%m/%Y %I:%M:%S %p") + " Error: " + (str(msg)))
            target.write('\n')
            target.close()
        