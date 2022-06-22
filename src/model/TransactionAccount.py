from genericpath import exists
from src.lib.DataConnection import DataConnection


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
        self.category_fk = list_form[4]

    def __eq__(self, other): 
        if not isinstance(other, TransactionAccount):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return (self.operation_date == other.operation_date 
        and self.value_date == other.value_date 
        and self.wording == other.wording
        and self.amount == other.amount
        and self.category_fk == other.category_fk
        and self.account_fk == other.account_fk)


class TransactionAccountRepository: 
    def __init__(self, connexion_db = None) -> None:
        if connexion_db is None:
            self.connexion_db = DataConnection.get_data_connexion()
        else:
            self.connexion_db = connexion_db

    def check_and_load(self, data_transform,account_id, last_date_check ): 
        last_transaction_download = self.get_transaction(account_id, last_date_check)
        #check si double ou triple by deleting
        data_to_load = self.check_already_present(last_transaction_download, data_transform)

    def check_already_present(self, last_transaction_download, data_transform):
        data_to_load = []
        for data_ready in data_transform:
            if data_ready in last_transaction_download: 
                last_transaction_download.remove(data_ready)
            else: 
                TransactionAccount(data_ready)
                data_to_load.append(data_ready)
        return data_to_load


    def get_transaction(self,account_id, last_date_transaction): 
        query = """
        Select operation_date, 
        value_date, 
        wording, 
        amount,
        category_fk from transaction_account
        where transaction_account.account_fk == %s ans operation_date <= %s"""
        cursor = self.connexion_db.cursor()
        cursor.execute(query, (account_id,last_date_transaction))
        result = cursor.fetchall()
        cursor.close()
        result = [TransactionAccount(list_form = transaction, account_id= account_id) for transaction in result]
        return result

    def push_transaction(self,account_id, data_to_load): 
        #TODO import 
        
        query = """
        INSERT INTO operation_date, 
        value_date, 
        wording, 
        amount,
        category_fk from transaction_account
        where transaction_account.account_fk == %s ans operation_date <= %s"""
        cursor = self.connexion_db.cursor()
        cursor.execute(query, (account_id,last_date_transaction))
        result = cursor.fetchall()
        cursor.close()
        return result


#todo
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()