# Get file from directory
# open, read csv file 
# transform data to make them ready to import
# import data. 
from src.model.get_csv_data import get_csv_data_from_file, get_list_file_from_directory
from src.model.Account import Account
from config import DIRECTORY

import os
# cmb : colonne 5, titre : RELEVE_COMPTE_CHEQUES_1_2022_06_13_04_25_21.csv
# boursorama : colonne 10, titre : export-operations-14-06-2022_20-27-03.csv

def transform_data(data_csv, title_file):


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

