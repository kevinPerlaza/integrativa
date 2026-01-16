class sesion:
    alumno = int
    profesor = []
class persona:
    run = ""
    nombre = ""
    apellido = ""
    edad = ""
    asignatura = ""
    rol = ["alumno","profesor"]
    sesion = sesion()

lista_usuarios = []
def ingresar_usuario():
    print("INGRESAR USUARIO \n")
    print("1. Ingresar Alumno")
    print("2. Ingresar Profesor")
    print("0. Volver al menú principal")
    opcion = input("\nSeleccione una opción: ")
    if opcion == "1":
        alumno = persona()
        alumno.run = input("Ingrese el RUN:")
        alumno.nombre = input("Ingrese el nombre:")
        alumno.apellido = input("Ingrese el apellido:")
        alumno.edad = input("Ingrese la edad:")
        alumno.asignatura = input("Ingrese la asignatura:")
        alumno.rol = "alumno"
        alumno.sesion.alumno = int(input("Ingrese la sección: "))
        lista_usuarios.append(alumno)
        print("\n Alumno",alumno.nombre,"",alumno.apellido,"",alumno.run," ingresado exitosamente!")
    elif opcion == "2":
        profesor = persona()
        profesor.run = input("Ingrese el RUN:")
        profesor.nombre = input("Ingrese el nombre:")
        profesor.apellido = input("Ingrese el apellido:")
        profesor.edad = input("Ingrese la edad:")
        profesor.asignatura = input("Ingrese la asignatura:")
        profesor.rol = "profesor"
        while True:
            sesion = int(input("Ingrese la sección: "))
            if sesion not in profesor.sesion.profesor:
                profesor.sesion.profesor.append(sesion)
                print("\n Sección",sesion," agregada exitosamente!")
            else:
                print("\n Sección",sesion," ya existe. Intente nuevamente.")
            respuesta = input(print("\n ¿Desea agregar otra sección? (si/no)"))
            if respuesta == "no":
                break
        lista_usuarios.append(profesor)
        print("\n Profesor",profesor.nombre,"",profesor.apellido," ingresado exitosamente!")
    elif opcion == "0":
        return
    else:
        print("\n Opción no válida. Intente nuevamente.")

def menu_principal():
    while True:
        print("Menu Principal \n")
        print("1. Ingresar usuarios")
        print("2. Ingresar notas")
        print("3. Listar Secciones")
        print("4. Listar Alumno")
        print("5. Listar Profesores")
        print("0. Salir")
        print("="*50)
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            ingresar_usuario()
        elif opcion == "2":
            ingresar_notas()
        elif opcion == "3":
            listar_secciones()
        elif opcion == "4":
            listar_alumno()
        elif opcion == "5":
            listar_profesores()
        elif opcion == "6":
            print("\n¡Hasta luego!")
            break
        else:
            print("\n Opción no válida. Intente nuevamente.")

menu_principal()
