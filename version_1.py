import os
lista_usuarios = []
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

def verificar_run(run):
    if lista_usuarios != []:
        for usuario in lista_usuarios:
            if usuario.run != run:
                return True
                break
        return print(" El Run ya existe en el sistema."), os.system("pause"), ingresar_usuario()
    run_usuario = run
    run_limpio = run_usuario.replace(".", "")
    tiene_guion = 0
    for digito in run_limpio:
        if digito == "-":
            tiene_guion = 1
    if tiene_guion == 0:
        print("Por favor, ingrese el RUN con el formato correcto (12345678-9).")
        return False
    parte_numero, dv_usuario = run_limpio.split("-") 
    serie = 2
    suma = 0
    for digito in reversed(parte_numero):
        if digito.isalpha():
            print("El RUN es INVÁLIDO, debe contener solo números. Ingrese nuevamente")
            return False   
        suma += int(digito) * serie
        serie += 1
        if serie > 7:
            serie = 2
    resto = 11 - (suma % 11)
    if resto == 11:
        dv_calculado = '0'
    elif resto == 10:
        dv_calculado = 'K'
    else:
        dv_calculado = str(resto)
    if dv_usuario.upper() == dv_calculado:
        return True
    else:
        print("Verificador del RUN es INVÁLIDO, Por favor, ingrese nuevamente")
        return False

def ingresar_usuario():
    print("INGRESAR USUARIO \n")
    print("1. Ingresar Alumno")
    print("2. Ingresar Profesor")
    print("0. Volver al menú principal")
    opcion = input("\nSeleccione una opción: ")
    if opcion == "1":
        alumno = persona()
        run = input("Ingrese el RUN (Formato: 12345678-9): ")

        while verificar_run(run) == False:
            run = input("Ingrese el RUN (Formato: 12345678-9): ")
        alumno.run = run
        alumno.nombre = input("Ingrese el nombre: ")
        alumno.apellido = input("Ingrese el apellido: ")
        alumno.edad = input("Ingrese la edad: ")
        alumno.asignatura = input("Ingrese la asignatura: ")
        alumno.rol = "alumno"
        alumno.sesion.alumno = int(input("Ingrese la sección: "))
        alumno.notas = []
        lista_usuarios.append(alumno)
        print("\n Alumno",alumno.nombre,"",alumno.apellido,"",alumno.run," ingresado exitosamente!")
    elif opcion == "2":
        profesor = persona()
        run = input("Ingrese el RUN (Formato: 12345678-9): ")
        while verificar_run(run) == False:
            run = input("Ingrese el RUN (Formato: 12345678-9): ")
        profesor.run = run
        profesor.nombre = input("Ingrese el nombre: ")
        profesor.apellido = input("Ingrese el apellido: ")
        profesor.edad = input("Ingrese la edad: ")
        profesor.asignatura = input("Ingrese la asignatura: ")
        profesor.rol = "profesor"
        while True:
            sesion = int(input("Ingrese la sección: "))
            if sesion not in profesor.sesion.profesor:
                profesor.sesion.profesor.append(sesion)
                print("\n Sección",sesion," agregada exitosamente!")
            else:
                print("\n Sección",sesion," ya existe. Intente nuevamente.")
            respuesta = input("\n ¿Desea agregar otra sección? (si/no): ")
            if respuesta == "no":
                break
        lista_usuarios.append(profesor)
        print("\n Profesor",profesor.nombre,"",profesor.apellido," ingresado exitosamente!")
    elif opcion == "0":
        return
    else:
        print("\n Opción no válida. Intente nuevamente.")

def verificar_run_profesor():
    run = input("Ingrese su RUN profesor: ")
    for usuario in lista_usuarios:
        if usuario.run == run:
            if usuario.rol == "profesor":
                print("\n Bienvenido, profesor ",usuario.nombre," ",usuario.apellido)
                return True
                break
    return False

def verificar_run_alumno():
    run = input("Ingrese RUN del alumno: ")
    for usuario in lista_usuarios:
        if usuario.run == run:
            if usuario.rol == "alumno":
                if usuario.sesion.alumno == int(input("Ingrese la sección: ")):
                    return True
                    break
    return False

def ingresar_notas():
    for usuario in lista_usuarios:
        if usuario.rol == "profesor":
            return True
            break
    return print(" No hay profesores ingresados, por favor ingrese un profesor"), os.system("pause"), menu_principal()

    while verificar_run_profesor() == False:
        print("\n El profesor no existe. Intente nuevamente.")
    
    run_alumno = input("Ingrese RUN del alumno para agregar notas: ")
    alumno_encontrado = None
    
    for usuario in lista_usuarios:
        if usuario.run == run_alumno and usuario.rol == "alumno":
            alumno_encontrado = usuario
            break
    
    if alumno_encontrado == None:
        print("\n El alumno no existe. Intente nuevamente.")
        return
    
    print("\nIngresando notas para:", alumno_encontrado.nombre, alumno_encontrado.apellido)
    alumno_encontrado.notas = []
    
    contador = 1
    while contador <= 3:
        nota_texto = input("Ingrese la Nota " + str(contador) + " (1.0 a 7.0): ")
        nota = float(nota_texto)
        if nota >= 1.0 and nota <= 7.0:
            alumno_encontrado.notas.append(nota)
            contador = contador + 1
        else:
            print("La nota debe estar entre 1.0 y 7.0. Intente nuevamente.")
    
    print("\n Notas ingresadas exitosamente para", alumno_encontrado.nombre, alumno_encontrado.apellido)

def listar_secciones():
    seccion_buscar = int(input("Ingrese la sección a listar: "))
    alumnos_seccion = []
    for usuario in lista_usuarios:
        if usuario.rol == "alumno" and usuario.sesion.alumno == seccion_buscar:
            alumnos_seccion.append(usuario)
    if len(alumnos_seccion) == 0:
        print("\nNo hay alumnos en la sección", seccion_buscar)
        return
    
    print("\n" + "=" * 85)
    print("LISTADO DE ALUMNOS - SECCIÓN", seccion_buscar)
    print("=" * 85)
    print("{:<20} {:>8} {:>8} {:>8} {:>10} {:>18}".format(
        "Nombre", "Nota 1", "Nota 2", "Nota 3", "Promedio", "Estado del Alumno"))
    print("-" * 85)
    
    for alumno in alumnos_seccion:
        nombre_completo = alumno.nombre + " " + alumno.apellido
        if len(alumno.notas) == 3:
            nota1 = alumno.notas[0]
            nota2 = alumno.notas[1]
            nota3 = alumno.notas[2]
            promedio = int((nota1 + nota2 + nota3) / 3 * 10) / 10
            if promedio >= 4.0:
                estado = "Aprobado"
            else:
                estado = "Reprobado"
            print("{:<20} {:>8.1f} {:>8.1f} {:>8.1f} {:>10.1f} {:>18}".format(
                nombre_completo, nota1, nota2, nota3, promedio, estado))
        else:
            print("{:<20} {:>8} {:>8} {:>8} {:>10} {:>18}".format(
                nombre_completo, "S/N", "S/N", "S/N", "S/N", "Sin notas"))
    
    print("=" * 85)
    print()
    input("Presione Enter para volver al menú principal...")

def menu_principal():
    while True:
        print("Menu Principal \n")
        print("1. Ingresar usuarios")
        print("2. Ingresar notas")
        print("3. Listar Secciones")
        print("4. Listar Alumnos")
        print("5. Listar Profesores")
        print("6. Salir")
        print("="*50)
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            ingresar_usuario()
        elif opcion == "2":
            ingresar_notas()
        elif opcion == "3":
            listar_secciones()
        elif opcion == "4":
            listar_alumnos()
        elif opcion == "5":
            listar_profesores()
        elif opcion == "6":
            print("\n¡Hasta luego!")
            break
        else:
            print("\n Opción no válida. Intente nuevamente.")

menu_principal()
