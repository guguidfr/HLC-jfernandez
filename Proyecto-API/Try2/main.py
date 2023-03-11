"""
Sentencias SQL para crear la tabla necesaria e insertar datos
DROP TABLE IF EXISTS LIBROS;
CREATE TABLE LIBROS(
	id INT AUTO_INCREMENT PRIMARY KEY,
	ISBN CHAR(13) NOT NULL UNIQUE,
	Titulo VARCHAR(100) NOT NULL,
	Autor VARCHAR(100) NOT NULL,
	Genero ENUM("Aventura","Fantasia","Ciencia-ficcion","Biografia") NOT NULL,
	Fecha_salida DATE NOT NULL
);

INSERT INTO LIBROS (ISBN, Titulo, Autor, Genero, Fecha_salida) VALUES
("9788498389369", "Harry Potter y la piedra filosofal", "J.K. Rowling", "Fantasia", "2001-01-01"),
("9788498389260", "Harry Potter y la cámara secreta", "J.K. Rowling", "Fantasia", "2002-01-01"),
("9788498389796", "Harry Potter y la Orden del Fénix", "J.K. Rowling", "Fantasia", "2003-01-01"),
("9788498387976", "Juego de Tronos", "George R.R. Martin", "Aventura", "2004-01-01"),
("9788498388973", "Choque de Reyes", "George R.R. Martin", "Aventura", "2005-01-01"),
("9788498389222", "Canción de Hielo y Fuego", "George R.R. Martin", "Aventura", "2006-01-01"),
("9788498389451", "Ready Player One", "Ernest Cline", "Ciencia-ficcion", "2007-01-01"),
("9788498389673", "El marciano", "Andy Weir", "Ciencia-ficcion", "2008-01-01"),
("9788498389543", "La guerra de los mundos", "H.G. Wells", "Ciencia-ficcion", "2009-01-01"),
("9788498389116", "La vida de Pi", "Yann Martel", "Aventura", "2010-01-01"),
("9788498389338", "El hobbit", "J.R.R. Tolkien", "Fantasia", "2011-01-01"),
("9788498389918", "El Señor de los Anillos: La comunidad del anillo", "J.R.R. Tolkien", "Fantasia", "2012-01-01"),
("9788498389758", "El Señor de los Anillos: Las dos torres", "J.R.R. Tolkien", "Fantasia", "2013-01-01"),
("9788498389031", "El Señor de los Anillos: El retorno del Rey", "J.R.R. Tolkien", "Fantasia", "2014-01-01"),
("9788498389642", "1984", "George Orwell", "Ciencia-ficcion", "2015-01-01"),
("9788498389161", "Un mundo feliz", "Aldous Huxley", "Ciencia-ficcion", "2016-01-01"),
("9788498389079", "Crónica del pájaro que da cuerda al mundo", "Haruki Murakami", "Biografia", "2017-01-01"),
("9788498389802", "De ratones y hombres", "John Steinbeck", "Biografia", "2018-01-01"),
("9788498389727", "La naranja mecánica", "Anthony Burgess", "Ciencia-ficcion", "2019-01-01"),
("9788498389680", "El código Da Vinci", "Dan Brown", "Aventura", "2020-01-01"),
("9788498389895", "El niño con el pijama de rayas","John Boyne", "Biografia", "2021-01-01"),
("9788498389017", "Los juegos del hambre", "Suzanne Collins", "Aventura", "2022-01-01"),
("9788498389321", "En llamas", "Suzanne Collins", "Aventura", "2023-01-01"),
("9788498389130", "Sinsajo", "Suzanne Collins", "Aventura", "2024-01-01"),
("9788498389437", "Los hombres que no amaban a las mujeres", "Stieg Larsson", "Aventura", "2025-01-01"),
("9788498389092", "El psicoanalista", "John Katzenbach", "Aventura", "2026-01-01"),
("9788498389734", "Cien años de soledad", "Gabriel García Márquez", "Biografia", "2027-01-01"),
("9788498389864", "El principito", "Antoine de Saint-Exupéry", "Aventura", "2028-01-01"),
("9788498389833", "El temor de un hombre sabio", "Patrick Rothfuss", "Fantasia", "2030-01-01"),
("9788498389628", "Canción de Hielo y Fuego: Tormenta de espadas", "George R.R. Martin", "Aventura", "2031-01-01"),
("9788498389246", "El hogar de Miss Peregrine para niños peculiares", "Ransom Riggs", "Fantasia", "2032-01-01");
"""

