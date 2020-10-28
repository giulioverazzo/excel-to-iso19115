import openpyxl
from data import Data
from utils import keyword_search, generate_XML
import sys

if __name__ == "__main__":
  # read excel file name
  excelfile = sys.argv[1]

  wb=openpyxl.load_workbook(excelfile)
  sheet=wb.worksheets[0]

  my_data = Data(sheet)
  XMLGenerated = generate_XML(my_data)

  filename = (".".join(excelfile.split(".")[:-1]))+".xml"
  
  with open(filename, 'w') as file_object:
    file_object.write(XMLGenerated)
  