# Description
A python script for convert and validate excel file to xml in iso19115 metadata format ready to be imported in Geonetwork 3.x

# Usage

First install the requirements with:
`pip install -r requirements.txt`

Then run like this:  
`python3 convert.py name-of-excel-file.xlsx`

The script is tailored to only read the `metadata-template.xlsx` file so, make a copy of it, change the value as needed and then proceed to convert it in xml.

The script will output a file named `name-of-excel-file.xml` that can be imported in Geonetwork 3.x

# Note

The script is a bit slow because it search for keywords occurrences in Nasa's GCMD. So its performances depends on how many keywords there are in the excel file.