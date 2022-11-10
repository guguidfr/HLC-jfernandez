# José Daniel Fernández López
# 10/11/2022
import csv
csv_file = "./Apuntes-introduccion/alumnos.csv"
alumno = ['Antonio','50','Córdoba']
with open(csv_file, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(alumno)