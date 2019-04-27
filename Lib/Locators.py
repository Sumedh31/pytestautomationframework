'''
Created on 01-Apr-2019

@author: Sumedh.Tambe
'''

import xlrd
from Lib.ExcelRead import ExcelRead

class Locators(ExcelRead):
    def Get_Locators(self):
        
        # This method should return the dictionary object
        # Dict object will have keys as Logical Name of the locator
        # Dict object will have values as property of the locator
        
        Dict = {}
        
        
        LlogicalName = self.Read_Col_Data("Locator")
#         print(LlogicalName)
        LProperty = self.Read_Col_Data("Property  ")
#         print(LProperty)
        
        for Index , Item in enumerate(LlogicalName):
            Dict[Item]= LProperty[Index]
        
        return  Dict