insert_init = [
        """
            INSERT INTO bank (id, wording, file_regex)
            VALUES (1, 'CMB', "RELEVE_COMPTE_CHEQUES_"), (2, 'Boursorama', "export-operations-")""",
        """
            INSERT INTO account (id, amount_available, wording, bank_fk, file_regex)
            VALUES (1, 0, "Compte commun CMB", 1, "RELEVE_COMPTE_CHEQUES_2"), 
            (2, 0, "Compte Megan CMB", 1, "RELEVE_COMPTE_CHEQUES_1"),
            (3, 0, "Compte Maxime CMB", 1, "RELEVE_COMPTE_CHEQUES_1"),
            (4, 0, "Compte Hayden CMB", 1, "RELEVE_COMPTE_CHEQUES_1"),
            (5, 0, "Compte Maxime Boursorama", 2, "export-operations"),
            """,
        """
            INSERT INTO budget_category (id, wording, detail, amount_planned)
            VALUES (1, "Divers", "Cadeau, autre",0), 
            ( 2 , "Video" , "Netflix - Serveur - Torrent", 0),
            ( 3 , "Assurance" , "Assurance maison - Voiture ", 0),
            ( 4 , "Banque" , "Frais bancaire", 0),
            ( 5 , "AideEtat" , "CAF,  Allocation ... ", 0),
            ( 6 , "Scolaire" , "Ecole, cantine", 0),
            ( 7 , "Impot" , "Taxe foncière ...", 0),
            ( 8 , "Electricite" , "EDF", 0),
            ( 9 , "Eau" , "Eau", 0),
            ( 10 , "Logement" , "Pret Maison", 0),
            ( 11 , "Transport" , "Essence, abonnement korrigo", 0),
            ( 12 , "Course" , "Alimentaire et usuel", 0),
            ( 13 , "Numerique" , "Portable / Internet", 0),
            ( 14 , "Virement interne" , "non pris en compte", 0),
            ( 15 , "Mis de côté" , "Reserve", 0),
            ( 16 , "Pertes et Profit" , "Entrée d'argent non attendu etc..", 0)
            
            
            
            """, 




        """
        INSERT INTO link_regex_category (id, regex, bank_fk, category_fk)
            VALUES (1, "logement", 1, 2)"""
]