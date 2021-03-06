from webbrowser import get
from config import banque
from src.model.BudgetCategory import BudgetCategoryRepository
from src.model.TransactionAccount import TransactionAccount
from decimal import Decimal
from datetime import datetime, date

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
        for line_transaction in data_csv: 
            transaction = TransactionAccount()
            transaction.category_fk = self.check_category_transaction(line_transaction, regex_link, config_banque["column_check_cat"])
            if "column_credit" in config_banque: 
                if line_transaction[config_banque["column_debit"]] == "":
                    transaction.amount = Decimal(line_transaction[config_banque["column_credit"]].replace(",", "."))
                else:
                    transaction.amount = - Decimal(line_transaction[config_banque["column_debit"]].replace(",", "."))
            else: 
                value = line_transaction[config_banque["column_debit"]].replace(" ", "")
                if "-" in line_transaction[config_banque["column_debit"]]: 
                    value = - Decimal(value.replace("-", "").replace(",","."))
                else :
                    value = Decimal(value.replace(",","."))
                transaction.amount = value
            transaction.wording = line_transaction[config_banque["column_libelle"]]
            #operation date
            operation_date = datetime.strptime(line_transaction[config_banque["column_operation_date"]], config_banque['format_date'])
            transaction.operation_date = date(operation_date.year, operation_date.month, operation_date.day)
            # value date
            value_date = datetime.strptime(line_transaction[config_banque["column_value_date"]], config_banque['format_date'])
            transaction.value_date = date(value_date.year, value_date.month, value_date.day)
            transaction.account_fk = self.account_id
            data_clean.append(transaction)
        return data_clean

    def check_category_transaction(self, transaction, regex_link, column_csv_to_check):
        regex = 0
        categorie = 1
        for line in regex_link: 
            if line[regex] in transaction[column_csv_to_check]: 
                return line[categorie]
        else: 
            return 1 #categorie Divers par d??faut initi?? au d??but de la BDD premi??re ligne

    def create_csv_to_load(self): 
        pass