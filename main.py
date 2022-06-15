# Get file from directory
# open, read csv file 
# transform data to make them ready to import
# import data. 

DIRECTORY = "/home/houlbert/Project/BudgetManagement/data/"

# cmb : colonne 5, titre : RELEVE_COMPTE_CHEQUES_1_2022_06_13_04_25_21.csv
# boursorama : colonne 10, titre : export-operations-14-06-2022_20-27-03.csv

import os
def get_list_file_from_directory(DIRECTORY):
    return os.listdir(DIRECTORY)


# compte 

import csv
def get_csv_data_from_file(path_file): 
    contenu = []
    with open(path_file, newline= '' ) as file: 
        reader = csv.DictReader(file)
        for row in reader: 
            contenu.append(row)
    return contenu

def check_origin(data_csv, title_file): 
    #TODO récupérer les infos en BDD plutôt
    # nom fichier, nombre colonne, nom de compte. 
    for key, value in origin.items(): 
        if len(data_csv[0]) == value["column"] and value["title"] in title_file:
            return key

def transform_data(data_csv, title_file):
    origin = check_origin(data_csv, title_file)


def main(): 
    files = get_list_file_from_directory(DIRECTORY)
    for title_file in files: 
        complete_path = DIRECTORY + title_file
        data_csv = get_csv_data_from_file(complete_path)
        transform_data(data_csv, title_file)
        add_data_to_the_list
    # import_data_in_db()

if __name__ == '__main__':
    main()

