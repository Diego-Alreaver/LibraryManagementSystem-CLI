import sys
from libreria import Libreria

def main():
    opc = ''
    libreria = Libreria("Libreria Al")
    libreria.agregarLibroCSV()
    libreria.agregarUsuarioCSV()

    while opc != '5':
        print(f"Bienvenido a la librería {libreria.nombre}, estas son sus opciones:")
        print("1) Agregar un libro")
        print("2) Revisar último libro agregado")
        print("3) Lista de usuarios")
        print("4) Buscar libro")
        print("5) Salir")
        
        opc = input("Seleccione una opción: ")

        # Validar que la opción sea un número y esté dentro de las opciones disponibles
        if opc not in ['1', '2', '3', '4', '5']:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            continue

        if opc == '1':
            libreria.agregarLibroManual()

        elif opc == '2':
            libreria.informacion() #muestra el último libro agregado

        elif opc == '3':
            libreria.listar_usuarios()

        elif opc == '4':
            subopcion = input("¿Cómo desea buscar el libro? \n1) Por título \n2) Por autor \n3) Por género \n4) Por año de publicación \n5) Volver al menú principal \n")
           
            if subopcion == '1':
                titulo = input("Ingrese el título: ")
                libros = libreria.buscarPorTitulo(titulo)
                if libros:
                    for libro in libros:
                        print(libro)
                        print("\n")
                else:
                    print("No se encontraron libros con ese título")
            
            elif subopcion == '2':
                autor = input("Ingrese el autor: ")
                libros = libreria.buscarPorAutor(autor)
                if libros:
                    for libro in libros:
                        print(libro)
                        print("\n")
                else:
                    print("No se encontraron libros de ese autor.")
            
            elif subopcion == '3':
                genero = input("Ingrese el género: ")
                libros = libreria.buscarPorGenero(genero)
                if libros:
                    for libro in libros:
                        print(libro)
                        print("\n")
                else:
                    print("No se encontraron libros de ese género")
            
            elif subopcion == '4':
                año = input("Ingrese el año de publicación: ")
                libros = libreria.buscarPorAño(año)
                if libros:
                    for libro in libros:
                        print(libro)
                        print("\n")
                else:
                    print("No se encontraron libros para ese año de publicación")
            elif subopcion == '5':
                break

        elif opc == '5':
            print("Saliendo del programa...")
            break

main()