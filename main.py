import openpyxl
from data import Data
from utils import keyword_search, generate_XML

if __name__ == "__main__":
  wb=openpyxl.load_workbook('test.xlsx')
  sheet=wb.worksheets[0]

  my_data = Data(sheet)
  generate_XML(my_data)
  