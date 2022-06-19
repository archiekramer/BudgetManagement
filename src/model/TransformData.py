class TransformData: 
    def __init__(self) -> None:
        pass
    
    def check_origin_account(self, data_csv, title_file): 
    #TODO récupérer les infos en BDD plutôt
    # nom fichier, nombre colonne, nom de compte. 
        for key, value in origin.items(): 
            if len(data_csv[0]) == value["column"] and value["title"] in title_file:
                return key
