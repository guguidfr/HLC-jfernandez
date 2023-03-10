"""
Sentencias SQL para crear la tabla necesaria e insertar datos
CREATE TABLE LIBROS(
	id INT PRIMARY KEY,
	ISBN CHAR(13) NOT NULL UNIQUE,
	Titulo VARCHAR(100) NOT NULL,
	Autor VARCHAR(100) NOT NULL,
	Genero ENUM("Aventura","Fantasia","Ciencia-ficcion","Biografia") NOT NULL,
	Fecha_salida DATE NOT NULL
);

INSERT INTO LIBROS (id, ISBN, Titulo, Autor, Genero, Fecha_salida) VALUES
(1, '9788401025230', 'Harry Potter y la piedra filosofal', 'J.K. Rowling', 'Fantasia', '1997-06-26'),
(2, '9788401025247', 'Harry Potter y la cámara secreta', 'J.K. Rowling', 'Fantasia', '1998-07-02'),
(3, '9788401025254', 'Harry Potter y el prisionero de Azkaban', 'J.K. Rowling', 'Fantasia', '1999-07-08'),
(4, '9788401025261', 'Harry Potter y el cáliz de fuego', 'J.K. Rowling', 'Fantasia', '2000-07-08'),
(5, '9788401025278', 'Harry Potter y la Orden del Fénix', 'J.K. Rowling', 'Fantasia', '2003-06-21'),
(6, '9788401025285', 'Harry Potter y el misterio del príncipe', 'J.K. Rowling', 'Fantasia', '2005-07-16'),
(7, '9788401025292', 'Harry Potter y las Reliquias de la Muerte', 'J.K. Rowling', 'Fantasia', '2007-07-21'),
(8, '9788408215906', 'El nombre del viento', 'Patrick Rothfuss', 'Fantasia', '2007-03-27'),
(9, '9788408216804', 'El temor de un hombre sabio', 'Patrick Rothfuss', 'Fantasia', '2011-11-04'),
(10, '9788498382549', 'Juego de tronos', 'George R.R. Martin', 'Fantasia', '1996-08-01'),
(11, '9788499082479', 'Choque de reyes', 'George R.R. Martin', 'Fantasia', '1998-11-16'),
(12, '9788496208002', 'Harry Potter y el legado maldito', 'J.K. Rowling', 'Fantasia', '2016-07-31'),
(13, '9788408043942', 'El retrato de Dorian Gray', 'Oscar Wilde', 'Biografia', '1890-07-01'),
(14, '9788417860213', 'La isla del tesoro', 'Robert Louis Stevenson', 'Aventura', '1883-11-14'),
(15, '9788466310583', 'Los pilares de la tierra', 'Ken Follett', 'Biografia', '1989-10-02'),
(16, '9788415130094', 'Matar a un ruiseñor', 'Harper Lee', 'Biografia', '1960-07-11'),
(17, '9788401467799', 'El diario de Ana Frank', 'Anne Frank', 'Biografia', '1947-06-25'),
(18, '9788497592208', 'El código Da Vinci', 'Dan Brown', 'Ciencia-Ficcion', '2003-03-18'),
(19, '9788408182185', 'La sombra del viento', 'Carlos Ruiz Zafón', 'Biografia', '2001-05-01');

"""

