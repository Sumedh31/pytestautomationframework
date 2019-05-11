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
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import chrome
from selenium.webdriver.common.proxy import Proxy,ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

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
            
            driver=webdriver
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
    def ChromeProxy(self):
        proxy=Proxy()
        proxy.proxy_type=ProxyType.MANUAL
        proxy.http_proxy="ipAddress:port"
        proxy.socks_proxy="ipAddress:port"
        proxy.ssl_proxy="ipAddress:port"
        cap=webdriver.DesiredCapabilities.CHROME        
        proxy.add_to_capabilities(cap)
        
        driver=webdriver.Chrome(desired_capabilities=cap)
        
        
        
        
        