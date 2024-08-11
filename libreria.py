from books import books
import csv

class Libreria:
    def __init__(self, nombre, capacidad_maxima=None):
        self.nombre = nombre #nombre de la libreria, para efectos estéticos
        self.libros = [] #lista donde se almacenaran todos los libros
        self.prestamos = [] #lista para saber los libros prestados
        self.capacidad_maxima = capacidad_maxima #capacidad maxima de la libreria, probablemente sin uso
        self.usuarios = [] #lista de nombres de usuarios registrados
 
    def agregarLibroCSV(self):
        with open("libros.csv", "r") as archivo_csv:
            lector = csv.reader(archivo_csv)
            for fila in lector:
                titulo = fila[0]
                autor = fila[1]
                genero = fila[2]
                año = fila[3]
                isbn = fila[4]
                disponibilidad = fila[5]
                nuevo_libro = books(titulo, autor, genero, año, isbn, disponibilidad)
                self.libros.append(nuevo_libro)

    def agregarLibroManual(self):
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        genero = input("Ingrese el género del libro: ")
        anio_publicacion = input("Ingrese el año de publicación del libro: ")
        isbn = input("Ingrese el ISBN del libro: ")
        estado = "Disponible"
        
        newbook = books(titulo, autor, genero, anio_publicacion, isbn, estado)
        self.libros.append(newbook)

        # Escribir los datos a un archivo CSV
        with open("libros.csv", "a", newline='') as archivo_csv:
            escritor = csv.writer(archivo_csv)
            # Convertir el objeto en una lista de sus atributos
            escritor.writerow([newbook._title, newbook._author, newbook._genre, 
                               newbook._publish_year, newbook._ISBN, newbook._disponible])
            
    def informacion(self):
        print(self.libros[len(self.libros)-1])
