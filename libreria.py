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
                print(fila)  # Imprime cada fila para verificar su contenido

