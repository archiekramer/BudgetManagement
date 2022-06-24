import mysql.connector, logging
from mysql.connector import Error
from config import INFO_CONNEXION_BDD

class DataConnection:
    connexion = None
    def __init__(self, host = INFO_CONNEXION_BDD["host"], database = INFO_CONNEXION_BDD["database"], 
    login = INFO_CONNEXION_BDD["username"], password = INFO_CONNEXION_BDD["mdp"]) -> None:
        self.host = host
        self.database = database
        self.login = login
        self.password = password

    def get_data_connexion(self): 
        if DataConnection.connexion is None: 
            DataConnection.connexion = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user= self.login,
                                                 password=self.password)
        return DataConnection.connexion

    def deco_bdd(self):
        if self.connexion.is_connected():
            self.connexion.close()
            logging.info("MySQL connection is closed")

    # def __new__(cls, *args, **kwargs):
    #     if not isinstance(cls.instance, cls):
    #         cls.instance = object.__new__(cls)
    #     return cls.instance