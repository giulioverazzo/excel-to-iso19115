# Description
A python script for convert and validate excel file to xml in iso19115 metadata format ready to be imported in Geonetwork 3.x

# Usage

Run like this:  
`python3 convert.py name-of-excel-file.xlsx`

The script will output a file named `name-of-excel-file.xml` that can be imported in Geonetwork 3.x

# Note

The script is a bit slow because it search for keywords occurrences in Nasa's GCMD. So its performances depends on how namy keywords there are in the excel file.