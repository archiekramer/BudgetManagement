from src.lib_spe.DataConnection import DataConnection


class BudgetCategory: 
    def __init__(self) -> None:
        pass

class BudgetCategoryRepository: 
    def __init__(self, connexion_db = None) -> None:
        if connexion_db is None:
            self.connexion_db = DataConnection().get_data_connexion()
        else:
            self.connexion_db = connexion_db

    def get_regex_link(self, bank_id): 
        query = """
        Select lrc.regex,
        lrc.category_fk from link_regex_category as lrc
        where bank_fk = %s """
        cursor = self.connexion_db.cursor()
        cursor.execute(query, (bank_id,))
        result = cursor.fetchall()
        cursor.close()
        return result
