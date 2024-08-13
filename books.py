

class books():
    def __init__(self, title, author, genre, publish_year, ISBN, disponible):
        self._title = title
        self._author = author
        self._genre = genre
        self._publish_year = publish_year
        self._ISBN = ISBN
        self._disponible = disponible

    def estado(self, prestamo):
        if prestamo == "Prestado":
            self._disponible = "Prestado"
        if prestamo == "Disponible":
            self._disponible = "Disponible"

    def __str__(self):
        return f" Título: {self._title}\n Autor: {self._author}\n Género: {self._genre}\n Año de publicación: {self._publish_year}\n ISBN: {self._ISBN}\n Disponibilidad: {self._disponible}"

    




