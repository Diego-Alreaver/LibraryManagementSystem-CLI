

class books():
    def __init__(self, title, author, genre, publish_year, ISBN, disponible = True):
        self._title = title
        self._author = author
        self._genre = genre
        self._publish_year = publish_year
        self._ISBN = ISBN
        self._disponible = disponible

    def estado(self, prestamo):
        if prestamo == "Prestado":
            self._disponible = False
        if prestamo == "Devuelto":
            self._disponible = True

    def __str__(self):
        return f"El título del libro es: {self._title}, su autor es: {self._author}, su género es: {self._genre}, su año de publicación es: {self._publish_year}, el ISBN es {self._ISBN}, el libro está {self._disponible}"

    




