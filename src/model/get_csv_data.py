import csv, os
from email.header import Header

def get_csv_data_from_file(path_file, withHeader = True): 
    contenu = []
    with open(path_file, newline= '' ) as file: 
        reader = csv.reader(file,delimiter=";")
        header = True
        for row in reader: 
            if header:
                header = False
                continue
            contenu.append(row)
    return contenu

def get_list_file_from_directory(DIRECTORY):
    return os.listdir(DIRECTORY)

    