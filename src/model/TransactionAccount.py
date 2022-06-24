from genericpath import exists
from src.lib_spe.DataConnection import DataConnection
from datetime import datetime

class TransactionAccount: 
    def __init__(self, operation_date = None, value_date = None, 
                        wording = None, amount = None, 
                        category_fk = None, account_id = None, list_form = None) -> None:
        self.operation_date = operation_date
        self.value_date  = value_date
        self.wording = wording
        self.amount = amount
        self.category_fk = category_fk
        self.account_fk = account_id
        if list_form is not None: 
            self.init_with_list(list_form)
    
    def init_with_list(self, list_form): 
        self.operation_date = list_form[0]
        self.value_date  = list_form[1]
        self.wording = list_form[2]
        self.amount = list_form[3]

    def __eq__(self, other): 
        if not isinstance(other, TransactionAccount):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return (self.operation_date == other.operation_date 
        and self.value_date == other.value_date 
        and self.wording == other.wording
        and self.amount == other.amount
        and self.account_fk == other.account_fk)

    def tuple_form(self): 
        return (self.operation_date, self.value_date, self.wording, self.amount, self.category_fk, self.account_fk)

class TransactionAccountRepository: 
    def __init__(self, connexion_db = None) -> None:
        self.connexion_db = DataConnection().get_data_connexion()

    def check_and_load(self, data_transform,account_id, last_date_check ): 
        last_transaction_download = self.get_transaction(account_id, last_date_check)
        #check si duplicate ou triple by deleting
        data_to_load =  self.check_already_present(last_transaction_download, data_transform)
        self.push_transaction(data_to_load)

    def check_already_present(self, last_transaction_download, data_transform):
        data_to_load = []
        for data_ready in data_transform:
            if data_ready in last_transaction_download: 
                last_transaction_download.remove(data_ready)
            else: 
                data_to_load.append(data_ready)
        return data_to_load


    def get_transaction(self,account_id, last_date_transaction): 
        query = """
        Select operation_date, 
        value_date, 
        wording, 
        amount
        from transaction_account
        where account_fk = %s and operation_date >= %s"""
        cursor = self.connexion_db.cursor()
        cursor.execute(query, (account_id, datetime.strftime(last_date_transaction, "%Y-%m-%d")))
        result = cursor.fetchall()
        cursor.close()
        result = [TransactionAccount(list_form = transaction, account_id= account_id) for transaction in result]
        return result

    def push_transaction(self, data_to_load): 
        query = """
        INSERT INTO transaction_account (operation_date, value_date, wording, amount, category_fk, account_fk)
        VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor = self.connexion_db.cursor()
        data_to_load = [elt.tuple_form() for elt in data_to_load]
        cursor.execute(query, data_to_load[0]) #[(,),(,)]
        cursor.close()
        self.connexion_db.commit()