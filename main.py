# Get file from directory
# open, read csv file 
# transform data to make them ready to import
# import data. 
from src.model.TransactionAccount import TransactionAccountRepository
from src.model.TransformData import TransformData
from src.model.get_csv_data import get_csv_data_from_file, get_list_file_from_directory
from src.model.Account import Account, AccountRepository
from config import DIRECTORY
import os, datetime
# cmb : colonne 5, titre : RELEVE_COMPTE_CHEQUES_1_2022_06_13_04_25_21.csv
# boursorama : colonne 10, titre : export-operations-14-06-2022_20-27-03.csv

last_date_check = datetime.datetime.now() - datetime.timedelta(days=5000)

def main(): 
    files = get_list_file_from_directory(DIRECTORY)
    for title_file in files:  
        complete_path = DIRECTORY + title_file 
        data_csv = get_csv_data_from_file(complete_path)
        #TODO offrir un autre mode de selection du compte et banque concerné par import genre selection dans liste. 
        bank_id, account_id = AccountRepository().get_origin_account_input(title_file)
        data_transform = TransformData(bank_id, account_id).transform_data(data_csv)
        TransactionAccountRepository().check_and_load(data_transform, account_id, last_date_check)
        
if __name__ == '__main__':
    main()

