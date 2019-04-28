'''
Created on 01-Apr-2019

@author: Sumedh.Tambe
'''
import xlrd
import sys

class ExcelRead():
    def __init__(self,ExcelFile,ExcelSheet):
        self.ExcelFile=ExcelFile
        self.ExcelSheet=ExcelSheet
        # Written code to
            # 1. Verify that excel file exists at the given location
            # 2. Verify that sheetName is present in the given excel file
            # 3. Open the Excel file 
            # 4. Raise exception in case of 1 , 2 and 3
        try:
            workbook=xlrd.open_workbook(self.ExcelFile)
          
        except IOError:
            print('Excel file not Present in the specified Path')
            sys.exit()
        else:
            try:
                self.Sheet=workbook.sheet_by_name(self.ExcelSheet)
            except IOError:                
                print("sheet " + ExcelSheet + " not present") 
                sys.exit()   
    
    def Row_Count(self): 
        return (self.Sheet.nrows-1)
    
    def Collumn_Count(self):
        Column_Name=self.Sheet.row_values(0)
        return(len(Column_Name))
        
    def Read_Col_Data(self,ColName):
            
            # Read the Column Names from the XL Sheet
                        
            column_name = self.Sheet.row_values(0)
            No_of_columns = len(column_name)
            
            #getting the column index for the particular ColName
            
            index = 0
            column_index = 0
            
            for i in range(0,No_of_columns):
                if column_name[i] == ColName:
                    index = index + 1
                    column_index = i
            
            #print column_index

        
            if index == 0:
                return ('Column Not Found')
            elif (index == 1):
                listu = []
                for rowval in range (1,self.Sheet.nrows):
                    listu.append(self.Sheet.cell_value(rowx=rowval,colx=column_index))
                return listu
            else:
                return ('There are more than one column with name ' + ColName)  
    def Read_Row_Data(self,RowNo):
            # Read the specified row data in the List            
            return self.Sheet.row_values(RowNo)       
                 
            
            