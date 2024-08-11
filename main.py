import sys
from libreria import Libreria

def main():
    opc = ''
    libreria = Libreria("Libreria Al")
    libreria.agregarLibroCSV()
    while opc != '5':
        print(f"Bienvenido a la librería {libreria.nombre}, estas son sus opciones:")
        print("1) Agregar un libro")
        print("2) Revisar último libro agregado")
        print("5) Salir")
        
        opc = input("Seleccione una opción: ")

        # Validar que la opción sea un número y esté dentro de las opciones disponibles
        if opc not in ['1', '2', '5']:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            continue

        if opc == '1':
            libreria.agregarLibroManual()
        elif opc == '2':
            libreria.informacion()
        elif opc == '5':
            print("Saliendo del programa...")
            break

main()