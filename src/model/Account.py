from logging import raiseExceptions
from src.lib_spe.DataConnection import DataConnection
from src.model.Bank import Bank
from src.model.Owner import Owner
from config import INFO_CONNEXION_BDD

class Account(Bank): 
    def __init__(self) -> None:
        self.id = int()
        self.wording = str()
        self.owner = Owner()

class AccountRepository: 
    def __init__(self, connexion_db = None) -> None:
        if connexion_db is None:
            self.connexion_db = DataConnection().get_data_connexion()
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
        on account.bank_fk = bank.id"""
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
        on account.bank_fk = bank.id"""
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
        result = self.get_bank_account_input_view()
        print("Voici la liste des comptes connues en BDD : ")
        account_ls = list(range(len(result)+1))
        for value in result: 
            bank_id, bank, account_id, account = value
            print("{compte_id} : Banque = {banque} // compte = {compte}".format(banque=bank, compte = account, compte_id = account_id))
            account_ls[account_id] = bank_id
        while True:
            print("veuillez choisir l'id du compte concerné par l'import du fichier {}".format(title_file))
            id = input()
            try: 
                id = int(id)
            except: 
                print("indiquez un chiffre")
            if id < len(account_ls) and id != 0: 
                break
        bank_id = account_ls[id]
        return bank_id, id