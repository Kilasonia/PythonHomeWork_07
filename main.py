from os.path import exists
from csv_creating import creating
from writing import writing_scv
from writing import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()
