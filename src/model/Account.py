from logging import raiseExceptions
from src.lib.DataConnection import DataConnection
from src.model.Bank import Bank
from src.model.Owner import Owner

class Account(Bank): 
    def __init__(self) -> None:
        self.id = int()
        self.wording = str()
        self.owner = Owner()

class AccountRepository: 
    def __init__(self, connexion_db = None) -> None:
        if connexion_db is None:
            self.connexion_db = DataConnection.get_data_connexion()
        else:
            self.connexion_db = connexion_db

    def get_account(id): 
        pass

    def get_origin_account(self):
        query = """
        Select bank.id, 
        bank.file_regex, 
        bank.file_column_number, 
        account.id, 
        account.wording_regex from account
        INNER JOIN bank 
        on account.bank_fk == bank.id"""
        cursor = self.connexion_db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def get_origin_account_in_dict(self):
        result = self.get_origin_account()
        result_dict = dict()
        for value in result: 
            bank_id, bank_file_regex,bank_file_column_number, account_id, account_regex = value
            if result_dict.has_key(bank_id):
                result_dict[bank_id] = {}
            bank = result_dict[bank_id]
            bank["bank_file_regex"] = bank_file_regex
            bank["column_number"] = bank_file_column_number
            bank[account_id] = {}
            bank[account_id]['account_regex'] = account_regex
        return result_dict

    def check_origin_account(self, data_csv, title_file): 
    # nom fichier, nombre colonne, nom de compte. 
        first_line = 0
        second_line = 1
        account_dict = self.get_origin_account_in_dict()
        for key_bank, bank in account_dict.items():
            if len(data_csv[0]) == bank["column_number"] and bank["bank_file_regex"] in title_file:
                bank_id = key_bank
            if data_csv[1][]

        if bank_id in locals() and 

        else:
            raise Exception("no account find")

