import mysql.connector, logging
from mysql.connector import Error
from mysql.connector.errors import OperationalError
from config import INFO_CONNEXION_BDD
import time

class DataConnection:
    connexion = None

    def __init__(self, host = INFO_CONNEXION_BDD["host"], database = INFO_CONNEXION_BDD["database"], 
    login = INFO_CONNEXION_BDD["username"], password = INFO_CONNEXION_BDD["mdp"]) -> None:
        self.host = host
        self.database = database
        self.login = login
        self.password = password
        self.connexion = None

    def get_data_connexion(self): 
            
        if DataConnection.connexion is None: 
            DataConnection.connexion = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user= self.login,
                                                 password=self.password)
        else :
            try: 
                cursor = DataConnection.connexion.cursor()
            except OperationalError:
                DataConnection.connexion = mysql.connector.connect(host=self.host,
                                                    database=self.database,
                                                    user= self.login,
                                                    password=self.password)
            else: 
                cursor.close()
        return DataConnection.connexion

    def deco_bdd(self):
        DataConnection.connexion.close()
        DataConnection.connexion = None
    
    def push(self, query): 
        self.connexion = DataConnection().get_data_connexion()
        cursor = self.connexion.cursor()
        cursor.execute(query)
        cursor.close()
        self.connexion.close()
        
    
    def push_commit(self, insert_init): 
        self.connexion = DataConnection().get_data_connexion()
        for query in insert_init:
            cursor = self.connexion.cursor()
            cursor.execute(query)
            self.connexion.commit()
            cursor.close()
        self.connexion.close()

