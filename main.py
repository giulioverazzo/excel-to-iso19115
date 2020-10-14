import openpyxl
from data import Data

if __name__ == "__main__":
  wb=openpyxl.load_workbook('test.xlsx')
  sheet=wb.worksheets[0]

  my_data = Data(sheet)

  print(my_data.pi_name)
  print(my_data.pi_email)
  print(my_data.pi_org)

  print(my_data.poc_name)
  print(my_data.poc_name)
  print(my_data.poc_name)    
