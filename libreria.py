from books import books
from usuarios import Usuario
import csv

class Libreria:
    def __init__(self, nombre, capacidad_maxima=None):
        self.nombre = nombre #nombre de la libreria, para efectos estéticos
        self.libros = [] #lista donde se almacenaran todos los libros
        self.prestamos = [] #lista para saber los libros prestados
        self.capacidad_maxima = capacidad_maxima #capacidad maxima de la libreria, probablemente sin uso
        self.usuarios = [] #lista de nombres de usuarios registrados

        #diccionarios para busquedas de libros
        self.catalogo_ISBN = {} #diccionario para buscar por ISBN
        self.catalogo_autores = {}  # Diccionario para búsqueda por autor
        self.catalogo_titulos = {}  # Diccionario para búsqueda por título
        self.catalogo_generos = {}  # Diccionario para búsqueda por género
        self.catalogo_año     = {}  # Diccionario para búsqueda por año de publicación
 

    def agregarUsuarioCSV(self):
        with open("usuarios.csv", "r") as archivo_csv:
            lector = csv.reader(archivo_csv)
            for fila in lector:
                nombre = fila[0]
                apellido = fila[1]
                cedula = fila[2]
                newuser = Usuario(nombre, apellido, cedula)
                self.usuarios.append(newuser)

    def agregarLibroCSV(self):
        with open("libros.csv", "r") as archivo_csv:
            lector = csv.reader(archivo_csv)
            libros = list(lector)
            # Ordenar la lista por el cuarto elemento de cada fila (año de publicación)
            fila = sorted(libros, key=lambda x: int(x[3]))
            with open('libros.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(fila)
        
            for fila in lector:
                titulo = fila[0]
                autor = fila[1]
                genero = fila[2]
                año = fila[3]
                isbn = fila[4]
                disponibilidad = fila[5]
                nuevo_libro = books(titulo, autor, genero, año, isbn, disponibilidad)
                self.libros.append(nuevo_libro)
                self.catalogo_ISBN[nuevo_libro._ISBN] = nuevo_libro

                if autor in self.catalogo_autores:
                    self.catalogo_autores[autor].append(nuevo_libro)
                else:
                    self.catalogo_autores[autor] = [nuevo_libro]
                
                if titulo in self.catalogo_titulos:
                    self.catalogo_titulos[titulo].append(nuevo_libro)
                else:
                    self.catalogo_titulos[titulo] = [nuevo_libro]

                if genero in self.catalogo_generos:
                    self.catalogo_generos[genero].append(nuevo_libro)
                else:
                    self.catalogo_generos[genero] = [nuevo_libro]

                if año in self.catalogo_año:
                    self.catalogo_año[año].append(nuevo_libro)
                else:
                    self.catalogo_año[año] = [nuevo_libro]

            

    def agregarLibroManual(self):
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        genero = input("Ingrese el género del libro: ")
        año = input("Ingrese el año de publicación del libro: ")
        isbn = input("Ingrese el ISBN del libro: ")
        estado = "Disponible"
        
        nuevo_libro = books(titulo, autor, genero, año, isbn, estado)
        self.libros.append(nuevo_libro)
        self.catalogo_ISBN[nuevo_libro._ISBN] = nuevo_libro


        if autor in self.catalogo_autores:
            self.catalogo_autores[autor].append(nuevo_libro)
        else:
            self.catalogo_autores[autor] = [nuevo_libro]
        
        if titulo in self.catalogo_titulos:
            self.catalogo_titulos[titulo].append(nuevo_libro)
        else:
            self.catalogo_titulos[titulo] = [nuevo_libro]

        if genero in self.catalogo_generos:
            self.catalogo_generos[genero].append(nuevo_libro)
        else:
            self.catalogo_generos[genero] = [nuevo_libro]

        if año in self.catalogo_año:
            self.catalogo_año[año].append(nuevo_libro)
        else:
            self.catalogo_año[año] = [nuevo_libro]

        # Escribir los datos a un archivo CSV
        with open("libros.csv", "a", newline='') as archivo_csv:
            escritor = csv.writer(archivo_csv)
            # Convertir el objeto en una lista de sus atributos
            escritor.writerow([nuevo_libro._title, nuevo_libro._author, nuevo_libro._genre, 
                               nuevo_libro._publish_year, nuevo_libro._ISBN, nuevo_libro._disponible])
            
    def inventarioTotal(self): #muestra todos los libros en la biblioteca
        for libro in self.libros:
            print(libro)
            print("\n")
        print(f"En total hay: {len(self.libros)} libros")

    def inventarioDisponible(self): #muestra solo libros disponibles
        for libro in self.libros:
            if libro._disponible == "Disponible":
                print(libro)
                print("\n")

    def inventarioPrestados(self):
        for libro in self.prestamos:
            for usuario in self.usuarios:  # Asumiendo que tienes una lista de usuarios
                if libro in usuario._libros_en_posesion:
                    print(f"{libro} \n En posesión de: {usuario._nombre} {usuario._apellido}")
                    break

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)
            if usuario._libros_en_posesion:
                print(f" El usuario {usuario._nombre} {usuario._apellido} posee los siguientes libros: ")
                for libro in usuario._libros_en_posesion:
                    print(f" {libro._title}")

            if usuario._historial_prestamo:
                print(f" El usuario {usuario._nombre} {usuario._apellido} anteriormente ha solicitado estos libros prestados y los ha devuelto con éxito: ")
                for libro in usuario._historial_prestamo:
                    print(f" {libro._title}")
            print("\n")
    
    def buscarPorISBN(self, isbn):
        if isbn in self.catalogo_ISBN:
            return self.catalogo_ISBN[isbn]
        else:
            return None
        
    def buscarPorAutor(self, autor):
        if autor in self.catalogo_autores:
            return self.catalogo_autores[autor]
        else:
            return []

    def buscarPorTitulo(self, titulo):
        if titulo in self.catalogo_titulos:
            return self.catalogo_titulos[titulo]
        else:
            return []
        
    def buscarPorGenero(self, genero):
        if genero in self.catalogo_generos:
            return self.catalogo_generos[genero]
        else:
            return []
        
    def buscarPorAño(self, año):
        if año in self.catalogo_año:
            return self.catalogo_año[año]
        else:
            return []
    
    def eliminarprestamo(self, isbn):
        libro = self.buscarPorISBN(isbn)
        if libro:
            for prestamo in self.prestamos:
                    if prestamo._ISBN == libro._ISBN:
                        self.prestamos.remove(prestamo)
                        break