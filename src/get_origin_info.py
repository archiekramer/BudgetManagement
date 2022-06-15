

from curses import has_key
from threading import activeCount


def get_origin_info(): 
    query = """
    Select bank.id, 
    bank.file_regex, 
    bank.file_column_number, 
    account.id, 
    account.wording_regex from account
    INNER JOIN bank 
    on account.bank_fk == bank.id"""
    try : 
        cursor = self.connexion.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
    except : 
        logging.critical("Erreur dans la recherche en BDD")
        logging.critical("requete en erreur : {}".format(query))
        logging.critical("attribut de la requete : {} - {} - {} - {} - ".format(taille, date, nom, parent))
    cursor.close()
    result_dict = dict()
    for value in result: 
        bank_id, bank_file_regex, account_id, account_regex = value
        # TODO check si key exist
        if result_dict[bank_id]
            result_dict[bank_id] = {}
        bank = result_dict[bank_id]
        bank["bank_file_regex"] = bank_file_regex
        bank[account_id] = account_regex
    return result_dict
