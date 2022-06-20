# Get file from directory
# open, read csv file 
# transform data to make them ready to import
# import data. 
from model.TransformData import TransformData
from src.model.get_csv_data import get_csv_data_from_file, get_list_file_from_directory
from src.model.Account import Account, AccountRepository
from config import BOURSORAMA, CMB, DIRECTORY

import os
# cmb : colonne 5, titre : RELEVE_COMPTE_CHEQUES_1_2022_06_13_04_25_21.csv
# boursorama : colonne 10, titre : export-operations-14-06-2022_20-27-03.csv



def main(): 
    files = get_list_file_from_directory(DIRECTORY)
    for title_file in files: 
        complete_path = DIRECTORY + title_file
        data_csv = get_csv_data_from_file(complete_path)
#        connexion_db = DataConnection.get_data_connexion()
        bank_id, account_id = AccountRepository().get_origin_account(title_file)
        data_transform = TransformData(bank_id, account_id).transform_data(data_csv,account_id)
        data_to_load = check_duplicate_before_import(data_transform)
        import_data
    # import_data_in_db()

if __name__ == '__main__':
    main()

