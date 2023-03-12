# José Daniel Fernández López
# 10/11/2022
import csv
csv_file = "./Apuntes-introduccion/alumnos.csv"
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    for linea in reader:
        print(linea)