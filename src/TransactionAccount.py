from src.lib.DataConnection import DataConnection


class TransactionAccount: 
    def __init__(self) -> None:
        pass

class TransactionAccountRepository: 
    def __init__(self, connexion_db = None) -> None:
        if connexion_db is None:
            self.connexion_db = DataConnection.get_data_connexion()
        else:
            self.connexion_db = connexion_db

    def check_duplicate_value(self, data_transform,account_id, last_date_check ): 
        pass

    def get_transaction(last_date_transaction): 
        query = """
        Select operation_date, 
        value_date, 
        wording, 
        amount,
        category_fk from transaction_account
        where transaction_account.account_fk == %s"""
        cursor = self.connexion_db.cursor()
        cursor.execute(query, (account_id,))
        result = cursor.fetchall()
        cursor.close()
        return result


