drop database budget_management; 
create database budget_management CHARACTER SET 'utf8'; 
use budget_management;

Create table budget_category (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    wording VARCHAR(100) NOT NULL,
    amount_planned DECIMAL(6,3),
    PRIMARY KEY (id)
);

Create table link_str_category (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    regex VARCHAR(100) NOT NULL,
        category_fk INT UNSIGNED NOT NULL,
    PRIMARY KEY (id)
);

Create table bank (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    wording VARCHAR(100) NOT NULL,
    file_regex VARCHAR(100) NOT NULL,
    file_nb_column INT UNSIGNED NOT NULL,
    account_name_id_column INT UNSIGNED NOT NULL, 
    PRIMARY KEY (id)
);


Create table account (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    amount_available DECIMAL(6,3),
    wording VARCHAR(100) NOT NULL,
    bank_fk INT UNSIGNED NOT NULL,
    wording_regex VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);


Create table transaction_bank(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    operation_date DATE,
    value_date DATE,
    wording VARCHAR(100) NOT NULL,
    amount DECIMAL(6,3),
    category_fk INT UNSIGNED NOT NULL,
    account_fk INT UNSIGNED NOT NULL,
    PRIMARY KEY (id),
    INDEX ind_date_operation (operation_date),
    INDEX ind_date_value (value_date),
    INDEX category_fk (category_fk),
    INDEX account_fk (account_fk)
);


Create table owner_account(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    wording VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);


ALTER TABLE bank ADD CONSTRAINT fk_bank_owner FOREIGN KEY (owner_fk) REFERENCES owner_account(id);
ALTER TABLE account ADD CONSTRAINT fk_account_bank FOREIGN KEY (bank_fk) REFERENCES bank(id);
ALTER TABLE account ADD CONSTRAINT fk_account_owner FOREIGN KEY (owner_fk) REFERENCES owner_account(id);
ALTER TABLE transaction_bank ADD CONSTRAINT fk_transaction_category FOREIGN KEY (category_fk) REFERENCES budget_category(id);
ALTER TABLE transaction_bank ADD CONSTRAINT fk_transaction_account FOREIGN KEY (account_fk) REFERENCES account(id);


INSERT INTO bank (id, wording, file_regex, file_nb_column, account_name_id_column)
VALUES ('1', 'CMB', "RELEVE_COMPTE_CHEQUES_",5, 4), ('2', 'Boursorama', "export-operations-",10, 9)
;

INSERT INTO account (id, amount_available, wording, bank_fk, wording_regex)
VALUES (1, 0, "Compte commun CMB", 1, "RELEVE_COMPTE_CHEQUES_2"), 
(2, 0, "Compte Megan CMB", 1, "RELEVE_COMPTE_CHEQUES_1"),
(3, 0, "Compte Maxime Boursorama", 2, "40129851");