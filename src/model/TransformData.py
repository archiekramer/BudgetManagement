from webbrowser import get
from config import CMB, BOURSORAMA
from model.BudgetCategory import BudgetCategoryRepository

class TransformData: 
    def __init__(self, bank_id) -> None:
        self.bank_id = bank_id
    
    def transform_data(self, data_csv):
        if bank_id == CMB["id"]: 
            data_to_load = tranformation_cmb(data_csv)
        elif bank_id == BOURSORAMA["id"] : 
            data_to_load = transformation_boursorama(data_csv)
        return data_to_load

    def get_regex_link(self, bank_id):
        return BudgetCategoryRepository().get_regex_link(bank_id)

    def tranformation_cmb(self, data_csv):
        regex_link= self.get_regex_link(CMB["id"])


    def transformation_boursorama(self, data_csv): 
        regex_link= self.get_regex_link(BOURSORAMA["id"])
