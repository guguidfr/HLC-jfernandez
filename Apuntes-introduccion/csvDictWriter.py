from csv import DictWriter, DictReader
men_names = []
file_men_names = "./Apuntes-introduccion/NombresComunesHombre.csv"
file_men_names_cpy = "./Apuntes-introduccion/NombresComunesHombre-Copy.csv"
file_header = ["Numero", "Nombre", "Frecuencia", "DeCadaMil"]
new_name = {"Numero":"101", "Nombre":"LEONARDO", "Frecuencia":"32.584", "DeCadaMil":"1,2"}
with open(file_men_names, 'r') as File:
    reader = DictReader(File)
    for row in reader:
        men_names.append(row)
#print(men_names)
with open(file_men_names_cpy, 'w', newline="") as File:
    writer = DictWriter(File, file_header)
    writer.writeheader()
    writer.writerows(men_names)
    writer.writerow(new_name)