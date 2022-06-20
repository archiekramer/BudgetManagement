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

    def get_bank_account_view(self):
        query = """
        Select bank.id, 
        bank.file_regex, 
        account.id, 
        account.wording_regex from account
        INNER JOIN bank 
        on account.bank_fk == bank.id"""
        cursor = self.connexion_db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def get_origin_account(self, title_file):
        result = self.get_origin_account()
        result_dict = dict()
        for value in result: 
            bank_id, bank_file_regex, account_id, account_regex = value
            if bank_file_regex in title_file and account_regex in title_file: 
                return bank_id, account_id
        else:
            raise BaseException

