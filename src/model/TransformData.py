from webbrowser import get
from config import banque
from model.BudgetCategory import BudgetCategoryRepository

class TransformData: 
    def __init__(self, bank_id, account_id) -> None:
        self.bank_id = bank_id
        self.account_id = account_id
    
    def transform_data(self, data_csv):
        regex_link = self.get_regex_link(self.bank_id)
        config_banque = banque[self.bank_id]
        data_to_load = self.tranformation(data_csv, regex_link, config_banque)
        return data_to_load

    def get_regex_link(self, bank_id):
        return BudgetCategoryRepository().get_regex_link(bank_id)

    def tranformation(self, data_csv, regex_link, config_banque):
        data_clean = []
        for transaction in data_csv: 
            categorie_fk = self.check_category_transaction(transaction, regex_link, config_banque["column_check_cat"])
            if "column_credit" in config_banque: 
                if transaction[config_banque["column_debit"]] is None:
                    amount = transaction[config_banque["column_credit"]]
                else:
                    amount = - transaction[config_banque["column_debit"]]
            else: 
                amount = transaction[config_banque["column_credit"]]
            wording = transaction[config_banque["column_libelle"]]
            operation_date = transaction[config_banque["column_operation_date"]]
            value_date = transaction[config_banque["column_value_date"]]
            account_fk = self.account_id
            data_clean.append(operation_date, value_date, wording, amount, categorie_fk, account_fk)
        return data_clean

    def check_category_transaction(self, transaction, regex_link, column_csv_to_check):
        regex = 0
        categorie = 1
        for line in regex_link: 
            if line[regex] in transaction[column_csv_to_check]: 
                return line[categorie]
        else: 
            return 0 #categorie Divers par défaut initié au début de la BDD première ligne

    def create_csv_to_load(self): 
        pass