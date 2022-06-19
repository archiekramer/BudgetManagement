import csv

def get_csv_data_from_file(path_file): 
    contenu = []
    with open(path_file, newline= '' ) as file: 
        reader = csv.DictReader(file)
        for row in reader: 
            contenu.append(row)
    return contenu

def get_list_file_from_directory(DIRECTORY):
    return os.listdir(DIRECTORY)

    