import sys
from libreria import Libreria

def main():
    libreria = Libreria("Libreria Al")
    libreria.agregarLibroCSV()
    libreria.informacion()


main()