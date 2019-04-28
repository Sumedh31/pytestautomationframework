'''
Created on 28-Apr-2019

@author: Sumedh.Tambe
'''
from Lib.ExcelRead import ExcelRead

class TestSuite(ExcelRead):
    
    def Get_Suite_DEtails(self):
        
        Details=[]
        
        RunMode=self.Read_Col_Data("RunMode")
        
        for index, I in enumerate(RunMode):
            if I.upper()=='YES':
                Details.append(self.Read_Row_Data(index+1))
            return Details