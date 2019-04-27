'''
Created on 09-Apr-2019

@author: Sumedh.Tambe
'''
from WebDrivers import BaseFunctionality
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
# from selenium import webdriver
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.CommonFunction=BaseFunctionality.BaseFunctionality()
        #self.LocatorsDict
        self.UtilObject,self.PyWorkingDirectory,self.Log,self.LocatorsDict,self.Driver,self.CONFIG,self.Wait=self.CommonFunction.InitializeValue()
     
    def test_1(self):
        self.CommonFunction.LoadUrl()
        self.Driver.get_screenshot_as_file("D:\GIT STuff\Test\cap.png")
        action=ActionBuilder(self.Driver)
        cookies=self.Driver.get_cookies()        
        print(cookies)
    
    def test_2(self):
        self.Log.Info("click on New Action button")
        #self.Wait.until(EC.element_to_be_clickable((By.XPATH, 'element.new_action_button'))).click()
        
    