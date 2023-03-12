from modules import checking
checking()

import subprocess
import requests as re
import json
import pandas as pd
import datetime

def bytes_to_dataframe(response_content):
    lista = json.loads(response_content)
    df = pd.DataFrame(lista)
    if df.empty:
        print("Sin datos")
    else:
        print(df)

'''
uvicorn_args = ["uvicorn", "uvicorn_server:app", "--host", "0.0.0.0", "--port", "8000"]
def start_server():
    server_process = subprocess.Popen(uvicorn_args)
    return server_process
def stop_server(server_process):
    server_process.terminate()
    server_process.wait()
'''

def delete():
    valid_entry = False
    while not valid_entry:
        try:
            target_id = int(input(("Introduce el id del registro que quieras borrar: ")))
        except ValueError:
            print("Debes de introducir un número.")
        else:
            url = f"http://localhost:8000/books/{target_id}"
            if re.delete(url).status_code == 404:
                print("El id que has elegido no corresponde con ningún libro.")
                valid_entry = True
            else:
                print(f"El libro con la id={target_id} se ha borrado correctamente")
                valid_entry = True

def select():
    valid_entry = False
    print("Puedes mostrar todos los libros o filtrar por autor y/o género. \n¿Qué quieres hacer? \n1: Mostrar todos los libros \n2: Filtrar por autor \n3: Filtrar por género \n4: Filtrar por autor y género \n5. Buscar por id \n6. Buscar por ISBN")
    while not valid_entry:
        try:
            option=int(input("--> "))
        except ValueError:
            print("Debes introducir un número")
        else:
            if option not in (1,2,3,4,5,6):
                print("Debes de elegir una de las opciones anteriores")
            else:
                valid_entry = True
    if option == 1: #type: ignore
        url = "http://localhost:8000/books"
        bytes = re.get(url).content
        bytes_to_dataframe(bytes)
    elif option == 2: #type: ignore
        autor = input("Escribe el nombre del autor/autora por el que quieres filtrar: ").replace(" ", "+")
        url = f"http://localhost:8000/books?author={autor}"
        bytes = re.get(url).content
        bytes_to_dataframe(bytes)
    elif option == 3: #type: ignore
        genero = input("Escribe el género por el que quieres filtrar: ").replace(" ", "+")
        url = f"http://localhost:8000/books?genre={genero}"
        bytes = re.get(url).content
        bytes_to_dataframe(bytes)
    elif option == 4: #type: ignore
        autor = input("Escribe el nombre del autor/autora por el que quieres filtrar: ").replace(" ", "+")
        genero = input("Escribe el género por el que quieres filtrar: ").replace(" ", "+")
        url = f"http://localhost:8000/books?author={autor}&genre={genero}"
        bytes = re.get(url).content
        bytes_to_dataframe(bytes)
    elif option == 5: #type: ignore
        valid_entry = False
        while not valid_entry:
            try:
                id=int(input("Introduce el id del libro que quieres buscar: "))
            except ValueError:
                print("Debes de introducir un número.")
            else:
                valid_entry = True
        url = f"http://localhost:8000/books/{id}" #type: ignore
        bytes = re.get(url).content
        bytes_to_dataframe(bytes)
    elif option == 6: #type: ignore
        valid_entry = False
        while not valid_entry:
            isbn=input("Introduce el ISBN del libro que quieres buscar: ")
            if isbn.isdigit() and len(isbn) == 13:
                valid_entry = True
            else:
                print("El ISBN debe de ser un número de 13 dígitos")
        url = f"http://localhost:8000/books/{isbn}" #type: ignore
        bytes = re.get(url).content
        bytes_to_dataframe(bytes)

def insert():
    new_entry = {}
    columns = ("id","isbn","title","author","genre","date")
    for column in columns:
        valid_entry = False
        while not valid_entry:
            if column == "id":
                try:
                    new_id=int(input("Introduce un número para la id del nuevo libro, o 0 para establecer uno automáticamente: "))
                except ValueError:
                    print("Debes de introducir un número.")
                else:
                    if new_id == 0:
                        valid_entry = True
                    else:
                        url = f"http://localhost:8000/{new_id}"
                        if re.get(url).status_code == 404:
                            new_entry["id"] = new_id
                            valid_entry = True
                        else:
                            print("El id que has introducido no está disponible.")
            elif column == "isbn":
                new_isbn = str(input("Introduce un ISBN. Debe de ser único: "))
                if new_isbn.isdigit() and len(new_isbn) == 13:
                    url = f"http://localhost:8000/{new_isbn}"
                    if re.get(url).status_code == 404:
                        new_entry["isbn"] = new_isbn
                        valid_entry = True
                    else:
                        print("El ISBN que has introducido no está disponible.")
            elif column == "title":
                new_entry["title"]=str(input("Introduce el título del libro: "))
                if len(new_entry["title"]) == 0 or len(new_entry["title"]) > 100:
                    print("El título no puede estar vacío, ni tener más de 100 caracteres.")
                else:
                    valid_entry = True
            elif column == "author":
                new_entry["author"]=str(input("Introduce el autor/autora del libro: "))
                if len(new_entry["author"]) == 0 or len(new_entry["author"]) > 100:
                    print("El autor/autora no puede estar vacío, ni tener más de 100 caracteres.")
                else:
                    valid_entry = True
            elif column == "genre":
                new_genre=str(input('Las opciones para los géneros del libro son: "Aventura","Fantasia","Ciencia-ficcion" y "Biografia". Puedes dejar el campo en blanco si no lo tienes claro: '))
                if len(new_genre) == 0:
                    print("No puedes dejar el género vacío")
                elif new_genre in ("Aventura","Fantasia","Ciencia-ficcion","Biografia"):
                    new_entry["genre"] = new_genre
                    valid_entry = True
                else:
                    print("Ese género literario no está en la lista.")
            elif column == "date":
                new_date=str(input('Introduce la fecha de salida del libro. Puedes dejar el campo en blanco si no lo tienes claro: '))
                if len(new_date) == 0:
                    print("No puedes dejar la fecha en blanco")
                elif len(new_date) > 0:
                    try:
                        datetime.date.fromisoformat(new_date)
                    except:
                        print("Debes introducir la fecha en el formato YYYY-MM-DD.")
                    else:
                        new_entry["date"] = new_date
                        valid_entry = True
                else:
                    print("Has introducido algo no válido")
    # print(new_entry)
    url = "http://localhost:8000/books"
    headers = {"Content-Type":"application/json"}
    response = re.post(url,headers=headers, data=json.dumps(new_entry))
    if response.status_code == 409:
        print("Ha habido un error al añadir un nuevo libro.")
    else:
        print("Se ha añadido correctamente el nuevo libro")
                        
def update():
    new_data = {}
    valid_entry = False
    while not valid_entry:
        try:
            id=int(input("Introduce el id del libro que quieres modificar: "))
        except ValueError:
            print("Debes de introducir un número.")
        else:
            valid_entry = True
    url = f"http://localhost:8000/books/{id}" #type: ignore
    if re.get(url).status_code == 404:
        print("El id que has elegido no corresponde con ningún libro.")
    else:
        valid_entry = True
    print("Puedes actualizar los valores: \n1. ISBN \n2. Título \n3. Autor \n4. Género \n5. Fecha de salida \nUsa (6) para salir y actualizar los datos.")
    update = False
    while not update:
        valid_option = False
        while not valid_option:
            try:
                option = int(input("Elige una opción (1.ISBN/2.Título/3.Autor/4.Género/5.Fecha de salida/6.Salir guardando los cambios)--> "))
            except ValueError:
                print("Debes de introducir un número")
            else:
                if option in range(1,7):
                    valid_option = True
                else:
                    print("Debes elegir una de las opciones anteriores")
        if option == 1: #type: ignore
            correct = False
            while not correct: 
                new_isbn = str(input("Introduce un nuevo ISBN: "))
                if new_isbn.isdigit() and len(new_isbn) == 13:
                    url_new = f"http://localhost:8000/books/{new_isbn}"
                    if re.get(url_new).status_code == 404:
                        new_data["isbn"] = new_isbn
                        correct = True
                    elif re.get(url).status_code == 200:
                        print("El ISBN que has introducido no está disponible.")
        elif option == 2: #type: ignore
            correct = False
            while not correct: 
                new_title = str(input("Introduce un nuevo título: "))
                if len(new_title) > 0 and len(new_title) < 100:
                    new_data["title"] = new_title
                    correct = True
        elif option == 3: #type: ignore
            correct = False
            while not correct: 
                new_author = str(input("Introduce un nuevo autor: "))
                if 100 > len(new_author) > 0 :
                    new_data["author"] = new_author
                    correct = True
        elif option == 4: #type: ignore
            correct = False
            while not correct: 
                new_genre = str(input('Introduce un nuevo género ("Aventura","Fantasia","Ciencia-ficcion","Biografia"): '))
                if 100 > len(new_genre) > 0 and new_genre in ("Aventura","Fantasia","Ciencia-ficcion","Biografia") :
                    new_data["genre"] = new_genre
                    correct = True
        elif option == 5: #type: ignore
            correct = False
            while not correct: 
                try:
                    new_date = str(datetime.date.fromisoformat(input("Introduce una nueva fecha: ")))
                except ValueError:
                    print('Debes de introducir una fecha válida en el formato "YYYY-MM-DD"')
                else:
                    new_data["date"] = new_date
                    correct = True
        elif option == 6: #type: ignore
            url = f"http://localhost:8000/books/{id}" #type: ignore
            re.put(url,data=json.dumps(new_data))
            update = True
            
         
if __name__ == '__main__':
    print("Iniciando el servidor...")
    server = subprocess.Popen(['python', 'uvicorn_server.py'], stdout=subprocess.PIPE , stderr=subprocess.PIPE) #
    finish = False
    print("La API de FastAPI conecta con una tabla de una base de datos. \n\nPuedes interactuar con ella con las siguientes opciones: \n1. Consultar la tabla \n2. Insertar un registro en la tabla \n3. Actualizar un registro de la tabla \n4. Borrar un registro de la tabla \nUsa (5) para salir.\n")
    while not finish:
        valid_option = False
        while not valid_option:
            try:
                action = int(input("Elige una de las opciones (1.SELECT/2.INSERT/3.UPDATE/4.DELETE/5.EXIT): "))
            except ValueError:
                print("Debes de introducir un número.")
            else:
                if action not in range (1,6):
                    print("Debes de elegir una de las opciones anteriores.")
                else:
                    valid_option = True
        if action == 1: #type: ignore
            select()
        elif action == 2: #type: ignore
            insert()
        elif action == 3: #type: ignore
            update()
        elif action == 4: #type: ignore
            delete()
        elif action == 5: #type: ignore
            print("Cerrando el servidor...")
            server.terminate()
            server.wait()
    # stop_server(server_process)
