'''
Created on 28-Apr-2019

@author: Sumedh.Tambe
'''
import unittest
import sys
from Lib import Utils
from Lib import TestSuite



if __name__=='__main__':
    UtilObject=Utils.Util()
    PythonWorkingDirectory=UtilObject.GetHomeDirectory()
    
    sys.path.append(PythonWorkingDirectory+"Testscripts")
    sys.path.append(PythonWorkingDirectory+"Lib")
    SuitObject=TestSuite.TestSuite(PythonWorkingDirectory+"TestSuite\TestSuite.xlsx","Suite")
    CurrentSuite=SuitObject.Get_Suite_DEtails()
    
    PyTestSuit=unittest.TestSuite()
        
    for TestCase in CurrentSuite:
        ClassName=TestCase[1]
        TestCaseName=TestCase[2]
        Import_Statement='from '+ClassName+ ' import '+ClassName
        
        exec(Import_Statement)
        print("PyTestSuit.addTest("+ClassName+"('"+TestCaseName+"'))")
        eval("PyTestSuit.addTest("+ClassName+"('"+TestCaseName+"'))")
    
