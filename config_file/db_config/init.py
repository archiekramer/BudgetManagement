reset_db = """
drop database budget_management; 
create database budget_management CHARACTER SET 'utf8'; 
use budget_management;

Create table budget_category (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    wording VARCHAR(100) NOT NULL,
    detail VARCHAR(100) NOT NULL,
    amount_planned DECIMAL(10,3),
    PRIMARY KEY (id)
);

Create table link_regex_category (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    regex VARCHAR(100) NOT NULL,
    bank_fk INT UNSIGNED NOT NULL,
    category_fk INT UNSIGNED NOT NULL,
    PRIMARY KEY (id)
);

Create table bank (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    wording VARCHAR(100) NOT NULL,
    file_regex VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);


Create table account (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    amount_available DECIMAL(10,3),
    wording VARCHAR(100) NOT NULL,
    bank_fk INT UNSIGNED NOT NULL,
    file_regex VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);


Create table transaction_account(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    operation_date DATE,
    value_date DATE,
    wording VARCHAR(100) NOT NULL,
    amount DECIMAL(10,3),
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

ALTER TABLE link_regex_category ADD CONSTRAINT fk_regex_bank FOREIGN KEY (bank_fk) REFERENCES bank(id);
ALTER TABLE link_regex_category ADD CONSTRAINT fk_regex_budget FOREIGN KEY (category_fk) REFERENCES budget_category(id);
ALTER TABLE account ADD CONSTRAINT fk_account_bank FOREIGN KEY (bank_fk) REFERENCES bank(id);
ALTER TABLE transaction_account ADD CONSTRAINT fk_transaction_category FOREIGN KEY (category_fk) REFERENCES budget_category(id);
ALTER TABLE transaction_account ADD CONSTRAINT fk_transaction_account FOREIGN KEY (account_fk) REFERENCES account(id);

"""

