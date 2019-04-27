'''
Created on 09-Apr-2019

@author: Sumedh.Tambe
'''
from selenium import webdriver
from Lib import Utils

import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote import mobile
from selenium.webdriver.remote.mobile import Mobile
import selenium
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import chrome

class BrowserInit():
    def __init__(self,Browser):
        self.Browser=Browser        
    
    def InitBrowser(self):
        CurrentWorkingDirectory=os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir))        
        
        if self.Browser=='CHROME':
            ChromeDriverPath=CurrentWorkingDirectory+'\Externals\drivers\chromedriver.exe'
            os.environ["webdriver.chrome.driver"]=ChromeDriverPath
            driver=webdriver.Chrome(ChromeDriverPath)
        elif self.Browser=='FireFox':
            driver=webdriver.Firefox()
        elif self.Browser=='IE':
            
            drivera=webdriver
        return driver
    
    def ChromeChangeDownloadPath(self):
        options=webdriver.ChromeOptions()
        
        prefs={"download.default_directory":"D:\Temp"}
        options.add_experimental_option("prefs", prefs)
        driver=webdriver.Chrome(chrome_options=options)
        
        return driver
    def ChromeMobileEmulator(self,URL):
        mobile_emulation={'devicename':'Nexus 5'}
        des=desired_capabilities.DesiredCapabilities.CHROME()        
        
        chromeoptions=webdriver.ChromeOptions()
        chromeoptions.a
        chromeoptions.add_experimental_option('mobileEmulation', mobile_emulation)             
        driver=webdriver.Remote(command_executor=URL,desired_capabilities=chromeoptions.to_capabilities())
        
        
        