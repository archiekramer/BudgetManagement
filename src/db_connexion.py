import mysql.connector
from mysql.connector import Error
from config import INFO_CONNEXION_BDD

class InteractionBdd:
    def __init__(self):
        self.database = INFO_CONNEXION_BDD["database"]
        self.user = INFO_CONNEXION_BDD["username"]
        self.password = INFO_CONNEXION_BDD["mdp"]
        self.connexion = self.connexion_bdd()


    def connexion_bdd(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=self.database,
                                                 user= self.user,
                                                 password=self.password)
            return connection

        except mysql.connector.Error as error:
            logging.critical("Failed to connect to in MySQL: {}".format(error))

    def deco_bdd(self):
        if self.connexion.is_connected():
            self.connexion.close()
            logging.info("MySQL connection is closed")

connexion_db = None

def get_connexion_bdd(): 
    if connexion is None: 
        connexion = InteractionBdd()
    return connexion.connexion