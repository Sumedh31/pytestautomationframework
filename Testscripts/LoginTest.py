'''
Created on 09-Apr-2019

@author: Sumedh.Tambe
'''
from WebDrivers import BaseFunctionality
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import autoit
# from selenium import webdriver
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.CommonFunction=BaseFunctionality.BaseFunctionality()
        #self.LocatorsDict
        self.UtilObject,self.PyWorkingDirectory,self.Log,self.LocatorsDict,self.Driver,self.CONFIG,self.Wait=self.CommonFunction.InitializeValue()
     
    def testthis(self):
        self.CommonFunction.LoadUrl()
        self.Driver.find_element(By.XPATH, self.LocatorsDict['FrontEndUsernameTextBox']).send_keys("guest1")
        self.Driver.find_element(By.XPATH, self.LocatorsDict['FrontEndPasswordTextBox']).send_keys("guest1")
        self.Driver.find_element(By.XPATH, self.LocatorsDict['FrontEndLoginButton']).click()
        self.Driver.get_screenshot_as_file("D:\GIT STuff\Test\cap.png")
        action=ActionChains(self.Driver)
        
        at=autoit()
        
        
        cookies=self.Driver.get_cookies()        
        print(cookies)
    
    def ABC(self):
        self.Log.Info("click on New Action button")
        #self.Wait.until(EC.element_to_be_clickable((By.XPATH, 'element.new_action_button'))).click()
        
    