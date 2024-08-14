import sys
from libreria import Libreria
from usuarios import Usuario

libreria = Libreria("Libreria Al")
libreria.agregarLibroCSV()
libreria.agregarUsuarioCSV()

def main():
    opc = ''
    while opc != '7':
        print(f"Bienvenido a la librería {libreria.nombre}, estas son sus opciones:")
        print("1) Agregar un libro")
        print("2) Inventario")
        print("3) Lista de usuarios")
        print("4) Buscar libro")
        print("5) Prestar un libro")
        print("6) Devolver un libro")
        print("7) Salir")
        
        opc = input("Seleccione una opción: ")

        # Validar que la opción sea un número y esté dentro de las opciones disponibles
        if opc not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            continue

        if opc == '1':
            libreria.agregarLibroManual()

        elif opc == '2':
            subopcion = input("\n1) Inventario total \n2) Inventario de solo disponibles \n3) Inventario de libros prestados \n4) Volver al menú principal \n")
            if subopcion == '1':
                libreria.inventarioTotal()

            elif subopcion == '2':
                libreria.inventarioDisponible()

            elif subopcion == '3':
                libreria.inventarioPrestados()
                    
            elif subopcion == '4':
                break


        elif opc == '3':
            libreria.listar_usuarios()

        elif opc == '4':
            while True:
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
                    break
                
                elif subopcion == '2':
                    autor = input("Ingrese el autor: ")
                    libros = libreria.buscarPorAutor(autor)
                    if libros:
                        for libro in libros:
                            print(libro)
                            print("\n")
                    else:
                        print("No se encontraron libros de ese autor.")
                    break
                
                elif subopcion == '3':
                    genero = input("Ingrese el género: ")
                    libros = libreria.buscarPorGenero(genero)
                    if libros:
                        for libro in libros:
                            print(libro)
                            print("\n")
                    else:
                        print("No se encontraron libros de ese género")
                    break
                
                elif subopcion == '4':
                    año = input("Ingrese el año de publicación: ")
                    libros = libreria.buscarPorAño(año)
                    if libros:
                        for libro in libros:
                            print(libro)
                            print("\n")
                    else:
                        print("No se encontraron libros para ese año de publicación")
                    break

                elif subopcion == '5':
                    break


        elif opc == '5':
            nombre = input("Ingrese el nombre del usuario al que se le prestará el libro: ")
            apellido = input("Ingrese el apellido de la persona: ")
            cedula = input("Ingrese la cédula de la persona: ")
            usuario_encontrado = False

            for usuario in libreria.usuarios:  # Recorre la lista de usuarios de la librería
                if usuario.verificacion(nombre, apellido, cedula):
                    print("\033[94mUsuario encontrado.\033[0m")
                    usuario_encontrado = True
                    libro_a_prestar = input("Ingrese el ISBN del libro a prestar: ")
                    libro = libreria.buscarPorISBN(libro_a_prestar)  # Buscar el libro por ISBN
                    if libro:
                        print(f"\033[94mLibro encontrado: {libro._title}\033[0m")
                        print(f"Estado actual del libro: {libro._disponible}")
                        if libro._disponible == "Disponible":  # Verificar que el libro esté disponible
                            usuario.prestarlibro(libro)
                            libreria.prestamos.append(libro)  # Registrar el préstamo en la librería
                            print(f"\033[92mLibro '{libro._title}' prestado exitosamente.\033[0m")
                        else:
                            print("\033[91mEl libro no está disponible.\033[0m")
                    else:
                        print("\033[91mEl libro no se encontró en la biblioteca.\033[0m")
                    break
            else:
                print("\033[91mUsuario no encontrado.\033[0m")


        elif opc == '6':
            nombre = input("Ingrese el nombre del usuario que desea devolver un libro: ")
            apellido = input("Ingrese el apellido de la persona: ")
            cedula = input("Ingrese la cédula de la persona: ")
            usuario_encontrado = False
            for usuario in libreria.usuarios:  # Recorre la lista de usuarios de la librería
                if usuario.verificacion(nombre, apellido, cedula):
                    print("\033[94mUsuario encontrado.\033[0m")
                    usuario_encontrado = True
                    usuario.listaprestados()
                    libro_a_devolver = input("Ingrese el ISBN del libro a devolver: ")
                    resultado = usuario.devolverlibro(libro_a_devolver)
                    print(resultado)
                    libreria.eliminarprestamo(libro_a_devolver) #eliminar el libro de la lista de prestados
 
        elif opc == '7':
            print("Saliendo del programa...")
            break

main()