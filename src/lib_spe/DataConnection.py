import mysql.connector
from mysql.connector import Error
from config import INFO_CONNEXION_BDD

class DataConnection:
    def __init__(self) -> None:
        self.connexion = None
        self.database = INFO_CONNEXION_BDD["database"]
        self.user = INFO_CONNEXION_BDD["username"]
        self.password = INFO_CONNEXION_BDD["mdp"]
    
    def get_data_connexion(self): 
        if self.connexion is None: 
            self.connexion = mysql.connector.connect(host='localhost',
                                                 database=self.database,
                                                 user= self.user,
                                                 password=self.password)
        return self.connexion

    def deco_bdd(self):
        if self.connexion.is_connected():
            self.connexion.close()
            logging.info("MySQL connection is closed")

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.instance, cls):
            cls.instance = object.__new__(cls)
        return cls.instance