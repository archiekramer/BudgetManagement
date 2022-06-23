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
        account.file_regex from account
        INNER JOIN bank 
        on account.bank_fk == bank.id"""
        cursor = self.connexion_db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def get_bank_account_input_view(self):
        query = """
        Select bank.id, 
        bank.wording, 
        account.id, 
        account.wording from account
        INNER JOIN bank 
        on account.bank_fk == bank.id"""
        cursor = self.connexion_db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    

    def get_origin_account(self, title_file):
        result = self.get_bank_account_view()
        for value in result: 
            bank_id, bank_file_regex, account_id, account_regex = value
            if bank_file_regex in title_file and account_regex in title_file: 
                return bank_id, account_id
        else:
            raise BaseException

    def get_origin_account_input(self, title_file): 
        result = self.get_bank_account_view()
        print("Voici la liste des comptes connues en BDD : ")
        account_ls = [range(len(result))]
        for value in result: 
            bank_id, bank, account_id, account = value
            print("Banque : {banque} banque_id : {banque_id} compte : {compte} compte_id : {compte_id}".format(banque=bank, 
            banque_id= bank_id, compte = account, compte_id = account_id))
            account_ls[account_id] = bank_id
        while True:
            print("veuillez choisir l'id du compte concerné par l'import du fichier {}".format(title_file))
            id = input()
            if id in account_ls: 
                break
        return account_ls[id], id