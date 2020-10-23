import openpyxl
from data import Data
from utils import keyword_search, generate_XML

if __name__ == "__main__":
  wb=openpyxl.load_workbook('test.xlsx')
  sheet=wb.worksheets[0]

  my_data = Data(sheet)
  XMLGenerated = generate_XML(my_data)

  filename = "metadata.xml"
  with open(filename, 'w') as file_object:
    file_object.write(XMLGenerated)
  