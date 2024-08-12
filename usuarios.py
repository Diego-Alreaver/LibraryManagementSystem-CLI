from books import books


class Usuario:
    def __init__(self, nombre, apellido, cedula):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._libros_en_posesion = []
        self._historial_prestamo = []


    def prestarlibro(self, libro):
        libro._disponible = "Prestado"
        self._libros_en_posesion.append(libro)
        self._historial_prestamo.append(libro)
        return f"Se le ha prestado el libro: {libro} al usuario {self._nombre} {self._apellido}"
        

    def devolverlibro(self, isbn):
        for libro in self._libros_en_posesion:
            if libro._ISBN == isbn:
                 libro._disponible = "Disponible"
                 self._libros_en_posesion.remove(libro)
                 return f"El usuario {self._nombre} {self._apellido} ha devuelto el libro {libro}"

    def __str__(self):
        return f" Nombre: {self._nombre} \n Apellido: {self._apellido} \n Cedula: {self._cedula}"