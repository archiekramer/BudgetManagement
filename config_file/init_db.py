import sys,os, time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import INFO_CONNEXION_BDD
from src.lib_spe.DataConnection import DataConnection
from db_config.init import reset_db
from db_config.insert_init import insert_init

connexion = DataConnection()
connexion.push(reset_db)
time.sleep(5)

connexion2 = DataConnection()
connexion2.push_commit(insert_init)