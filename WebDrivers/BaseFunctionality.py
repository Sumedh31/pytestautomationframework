from Lib.Utils import Util
from Lib.ConfigReader import Configuration
from Lib.Logger import Logger
from Lib.BrowserInit import BrowserInit
from Lib.Locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
import time

class BaseFunctionality():
    def __init__(self):
        self.UtilObject=Util()
        
        self.PyWorkingDirectory=self.UtilObject.GetHomeDirectory()
        self.CONFIG = Configuration(self.PyWorkingDirectory+"Config\AutoSetting.ini")
        self.Log_Level=self.CONFIG.ENV.LOG_LEVEL
        self.Log=Logger(self.Log_Level)
        self.Locate = Locators(self.PyWorkingDirectory+"OR\Locator.xlsx", "OR")
        self.LocatorsDict=self.Locate.Get_Locators()
        self.Log.Info("Initialization")
        self.Log.Info("opening URL")
        self.Browser=BrowserInit((self.CONFIG.ENV.BROWSER).upper())
        self.Driver=self.Browser.InitBrowser()
        self.Wait=WebDriverWait(self.Driver,20,poll_frequency=1)
        
    def InitializeValue(self):
        #self.LocatorsDict
        return(self.UtilObject,self.PyWorkingDirectory,self.Log,self.LocatorsDict,self.Driver,self.CONFIG,self.Wait)
    
    def LoadUrl(self):
        self.Driver.get(self.CONFIG.APPDETAILS.URL)
        self.Driver.maximize_window()
        
        
    
        
        
        