# FastAPI

Estos archivos te permiten iniciar un servidor de *Uvicorn* con una API de *FastAPI* que conecta a una base de datos de MySQL con una tabla *LIBROS*

> Puedes usar el archivo `sql_table.sql` para crear la tabla e insertar filas de ejemplo.
> 
> Si tu servidor es MariaDB en lugar de MySQL, tendrás que cambiar las líneas `1` y `2` del archivo `objetos.py`, todas las veces que aparezca `pymysql` por `mariadb` y los credenciales de inicio de sesión en la línea `7`.

Necesitarás los módulos:

- `fastapi`

- `uvicorn`

- `pymysql` o `mariadb`

- `pandas`

- `requests`

Para poder instalarlos debes tener `pip` en tu sistema. Puedes comentar las las líneas de la `1` a la `8` del archivo `main.py` si ya los tienes todos.

Si cumples con todos los requisitos, basta con que ejecutes el archivo `main.py` estando en el mismo directorio.

---

## objetos.py

Las funciones de este archivo son las que se encargan de interactuar con la base de datos.

Usa las librerías: `pymysql`/`mariadb`, `pandas` y `sys`.

Clases, métodos y funciones dentro el archivo:

- `class Book`: la tabla, al ser sobre libros, necesitamos una clase *Libro* que contenga la información de cada uno. Los atributos son las columnas de la tabla.

- `def fill_none_values(self, other_book)`: este método se usa cuando queremos actualizar un libro, ya que en el proceso crearemos un libro *"temporal"* que tendrá la información que el usuario ha pasado, y otro que es el que ha elegido para actualizar de la base de datos. Estos dos libros se comparan, y si en el libro *"temporal"* alguno de los atributos es *None*, se le asignará el valor que ya tenía (es decir, los datos del libro *"antiguo"*).

- `def add_book(self)`: método que hace un *`INSERT`* en la base de datos usando un cursor de `pymysql`. Usa los atributos del objetos en la sentencia.

- `def update_book(self,pk)`: además de recibir la información del libro *"temporal"*, recibe la clave primaria del libro que hay que actualizar. Antes de hacer el *`UPDATE`* llama al método `fill_none_valuess` para asegurar que todos los atributos tienen un valor. Usa un cursor de `pymysql`.

- `def js_to_book(js)`: función que transforma  un diccionario con la información que ha pasado el usuario a un objeto de la clase *Book*. Las claves que no estén en el diccionario que se ha pasado se crean automáticamente con el valor *None*.

- `def get_all_as_objects()`: se crea un tupla vacía, se hace un *`SELECT * FROM LIBROS`* usando `pandas` *(al usar `pandas`, obtenemos un "DataFrame", pero como no se puede devolver como respuesta, pasamos el "DataFrame" a una lista de diccionarios)* y se transforman los diccionarios usando `js_to_book` para luego añadirlos a una tupla, que es la que devuelve el servidor.

- `def get_by_genre_or_author(genre = None, author = None)`: obtiene la lista de libros de `get_all_as_objects` y elimina aquellos que no correspondan con la búsqueda usando un bucle *for* *(`book = [book for book in get_all_as_objects if book.genre == genre]`)*.
  
  > Este bucle devolverá una tupla de libros formada por el bucle *for* y el condicional *if book.genre == genre*.
  > 
  > Usar de esta manera las sentencias *for* e *if* permiten devolver listas o valores concretos escribiendo una línea fácilmente interpretable como "lenguaje natural"

- `def get_py_pk(pk)` y `def get_by_isbn(isbn)`: hacen lo mismo que la función anterior, pero comparando el *id* o *ISBN* de los libros.

- `def delete_book(pk)`: función que ejecuta una sentencia *`DELETE`* sobre la tabla.
  
  > Ejecutar un *DELETE* como el siguiente: `DELETE FROM LIBROS WHERE id = 777`, aunque no exista el libro con la id=777, se ejecutará igualmente. Para comprobar si se ha borrado alguna fila de la tabla, se usa en la línea `129` el método `rowcount`, que devuelve el número de filas eliminadas o insertadas; en este caso, si devuelve `0` significa que no se ha borrado ninguna fila, por lo que la sentencia *DELETE* que acabamos de ejecutar no ha borrado nada de la tabla.

---

## uvicorn_server.py

En este archivo se definen los *endpoints* a los que responderá la API. Usará las funciones del archivo anterior.

Usa las librerías `uvicorn` y `fastapi`.

Endpoints de la API:

- `@app.get("/books")`: este endpoint responde a las urls `http://localhost:8000/books`, `http://localhost:8000/books?genre=[género_de_tabla]`, `http://localhost:8000/books?author=[autor]` y `http://localhost:8000/books?genre=[génreo]&author=[autor]` mediante `GET`.  Ejecutará la función `get_all`, que llamará a las funciones `get_all_as_objects` si no recibe ningún parámetro de búsqueda, o `get_by_genre_or_author` si algún parámetro está presente. Y en caso de que tras hacer la solicitud a la base de datos no obtenga ninguna coincidencia, se mostrará el error 404 junto un mensaje indicando que no ha habido coincidencias con la búsqueda.
- `@app.get("/books/{value}")`: responde a la url `http://localhost:8000/books/[número]` mediante `GET`. Si el número que se pasa es de exactamente 13 dígitos, buscará por ISBN; en cualquier otro caso lo hará por id. Si no hay coincidencias devolverá el error 404 junto a un mensaje de que no existe el libro con el id o ISBN elegido.

> Si queremos interactuar con estos endpoints, podemos ejecutar el comando *curl* usando alguna de las urls anteriores. 
> 
> Por ejemplo: 
> 
> - `curl -X GET "http://localhost:8000/books"`
> 
> - `curl -X GET "http://localhost:8000/books?author=J.K.+Rowling"`
> 
> - `curl -X GET "http://localhost:8000/books?genre=Fantasia&author=J.K.+Rowling"`
> 
> - `curl -X GET "http://localhost:8000/books/1"`
> 
> - `curl -X GET "http://localhost:8000/books/1111111111111"`

- `@app.post("/books", status_code=status.HTTP_201_CREATED)`: responde a la url `http://localhost/books` mediante `POST`. El servidor recibirá datos en formato *json*, los transformará en un libro y usará el método`add_book` para añadirlo a la tabla. Si hay algún error se deberá *(normalmente)* a que ha habido un conflicto al insertar los datos, como un id o ISBN duplicado, en este caso.

> Para interactuar con este endpoint debemos usar *curl* de la siguiente manera:
> 
> `curl -X POST -H "Data-Type: application/json" -d '{"id":n, "isbn":"num_13_digitos", "title":"titulo_libro", "author":"autor_libro", "genre":"genero_libro", "release_date":"YYY-MM-DD"}' "http://localhost:8000/books`

- `@app.put("/books/{pk}")`: responde a la url `http://localhost:8000/books/[id]`. Hace exactamente lo mismo el endpoint anterior, solo que la petición es de tipo *PUT*, y el json que debemos pasar no tiene por qué tener todos las columnas de la tabla.

> Los únicos cambios respecto a usar curl con *POST* son:
> 
> - Cambiar *POST* por *PUT*.
> 
> - El json que debemos pasar puede tener o no todas las columnas correspondientes con sus respectivos valores.
> 
> - Hay que añadir el id del libro al final de la url. 
> 
> Ejemplo: `curl -X PUT -H "Data-Type: application/json" -d '{"clave":"valor"}' "[http://localhost:8000/books/[n]"`

- `@app.delete("/books/{pk}")`: responde a la misma url que el endpoint anterior. Se ejecutará la función `delte_book(pk)` con el id que hayamos pasado mediante url. La función devolverá un código de error `0` o `1` dependiendo de si se ha borrado de verdad un libro o no de la tabla; en el caso del `1`, error, se mostrará el error 404 por lo mencionado al explicar `delte_book(pk)`.

> Podemos usar curl de la siguiente manera para interactuar con la api: `curl -X DELETE "http://localhost:8000/books/1"`

Puedes "descomentar" la línea `86` si quieres ejecutar el servidor de manera independiente.

---

## main.py

Este archivo permite la ejecución simultánea del servidor de *uvicorn* y un programa para interactuar con el mismo.

Usa las librerías: `sys`, `subprocess`, `requests`, `json`, `pandas`, `datetime` y `time`

Al principio se importa la función `checking()` del archivo `modules.py` para comprobar que todas las librerías están presentes en el sistema.

> Puedes comentar de la línea `1` a la `8` si ya tienes las librerías.

Las funciones de este archivo se encargan de hacer solicitudes al servidor mediante la librería `requests`. Esta librería necesita normalmente 3 elementos para hacer solicitudes a un servidor, aunque cuando las hacemos mediante *GET* solamente necesitaremos uno *(la url)*. Estos elementos son:

- La url a la que vamos a hacer la solicitud. El atributo *url* de la solicitud.

- Definir el tipo de información que vamos a pasar. El atributo *headers* de la solicitud.

- La información que vamos a pasar. El atributo *data* de la solicitud.

Siempre que definamos una solicitud tenemos que especificar de qué tipo va a ser la solicitud. Estas pueden ser: *get*, *post*, *put* y *delete*.

Para definir una solicitud *GET* hacemos lo siguiente:

```python
url = "http://lpinocalhost:8000/books"
response = requests.get(url=url)
print(response.content) # Muestra en pantalla el contenido que ha devuelto el servidor. Suele ser código HTML.
```

> Normalmente se usa la librería `BeautyfulSoup` para *parsear* el código html que devuelve el servidor y así extraer información.

Para una solicitud *DELETE* es:

```python
url = "http://localhost:8000/books/1"
requests.delete(url=url)
```

Y para una solicitud *POST* o *PUT*:

```python
url_post = "http://localhost:8000/books"
headers = {"Data-Type": "application/json"}
content = {"id":n, "isbn":"num_13_digitos", "title":"titulo_libro", "author":"autor_libro", "genre":"genero_libro", "release_date":"YYY-MM-DD"}
# ---------------
requests.post(url=url_post, headers=headers, data=content)
# ---------------
url_put = "http://localhost:8000/books/1"
requests.put(url=url_put, headers=headers, data=content)
```

Todas estas respuestas contienen información a la que podemos acceder usando los atributos `.content`, `.headers` o `.status_code`, por ejemplo, aunque normalmente usaremos el primero pero para comprobar las respuestas del servidor necesitaremos el código de error que va en el `.status_code`. 

Las funciones de este archivo son:

- `def bytes_to_dataframe(response_content)`: recibe los bytes de las solicitudes de la función `select()` y los transforma a un *DataFrame* de pandas para poder representar la información en forma de tabla. Si el *DataFrame* no está vacío, lo imprime, en caso contrario muestra un mensaje diciendo que no hay datos.
  
  > Para poder llegar al *DataFrame*, antes debemos de usar la función `loads()` de la librería `json` para transformar los bytes que envía el servidor (sabemos que lo que envía el servidor es una lista de objetos, como podemos ver al hacer una solicitud con *curl*) a una lista de diccionarios que pandas puede procesar.

- `def delete()`: pide al usuario el id de un libro hace una solicitud *DELETE* al servidor; además comprueba el código de respuesta del servidor para informar al usuario si el libro se ha borrado, o no existe un libro con la id que ha introducido.

- `def select()`: es un menú que pide al usuario cómo quiere obtener la información de la tabla. Hay 6 opciones: mostrar todos, buscar por autor, buscar por género, buscar por id o buscar por ISBN. En caso de cada opción hace lo siguiente:
  
  1. Si es necesario, pide al usuario el valor o valores por los que filtrar.
  
  2. Hace una petición al servidor.
  
  3. Envía a `bytes_to_dataframe` los bytes que ha obtenido.

- `def insert()`: se crea un diccionario que va a tener tantos pares clave-valor como columnas tiene la tabla. Con un bucle *for* se recorrerá un menú que pedirá al usuario los datos necesarios para cada valor de la columna que vaya a insertar, además de hacer un control de error tanto de la entrada del usuario como de la disponibilidad del nuevo id e ISBN. Tras formar el diccionario con todos los valores necesarios, se hace una solicitud *POST* al servidor.

- `def update()`: es esencia lo mismo que la función `insert()`, solo que permite al usuario elegir los valores que quiere asignar.

### Cuerpo del archivo

Dentro del `if __name__ == '__main__'` encontramos la ejecución en segundo plano del servidor usando la librería `subprocess` *(se ha redirigido tanto la salida estándar como la de errores a nul (en Windows) o a /dev/null (en Linux) para así ocultar los mensajes del servidor)*.

Tras el inicio del servidor, comienza un bucle `while` que permitirá al usuario ejecutar las diferentes funciones antes mencionadas.

---

## modules.py

Es un script que creé hace un par de meses que me permite instalar de manera automática las librerías que necesito. Lo hice descubriendo librerías para un proyecto de descargar vídeos de redes sociales, y navegando por StackOverflow.

---

# Cómo lo he hecho

Partiendo de la API de ejemplo que usa un `.csv` de numerosos Pokémons y aprendiendo a usar pandas y el comando *curl*, he conseguido hacer los endpoints y funciones necesarias.

Ha sido principalmente ensayo y error junto a bastante tiempo leyendo la documentación oficial de las librerías.

Los endpoints han partido de lo mismo que en el de ejemplo: he partido de copiar y pegar los endpoints.

En cuanto a las funciones, ha sido mejorar con pandas las que usé en el CRUD de MariaDB.

Y para hacer el archivo principal, no ha sido demasiado difícil ya que hice algo parecido con mi proyecto de descargar vídeos (que está pausado, y retomaré en algún momento).

Respecto al uso de librerías, la que más me ha costado entender ha sido la de FastAPI, porque al leer la de ejemplo de los Pokémons, no había ni un sólo comentario, así que he ido bastante a ciegas. 
