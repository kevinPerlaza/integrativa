import os
lista_usuarios = []
class Persona:
    def __init__(self):
        self.run = ""
        self.nombre = ""
        self.apellido = ""
        self.edad = ""
        self.asignatura = ""

class Alumno:
    def __init__(self):
        self.persona = Persona()
        self.sesion = 0       
        self.rol = "alumno"
        self.notas = []          

class Profesor:
    def __init__(self):
        self.persona = Persona()
        self.rol = "profesor"
        self.sesion = []         

alumno1 = Alumno()
alumno1.persona.run = "11111111-1"
alumno1.persona.nombre = "kevin"
alumno1.persona.apellido = "perlaza"
alumno1.persona.edad = "24"
alumno1.persona.asignatura = "programacion"
alumno1.sesion = 1
lista_usuarios.append(alumno1)

profesor1 = Profesor()
profesor1.persona.run = "12345678-5"
profesor1.persona.nombre = "hansel"
profesor1.persona.apellido = "duran"
profesor1.persona.edad = "22"
profesor1.persona.asignatura = "programacion"
profesor1.sesion = [1,2]
lista_usuarios.append(profesor1)

def run_existe(run):
    if lista_usuarios != []:
        for usuario in lista_usuarios:
            if usuario.persona.run == run:
                print(" El Run ya existe en el sistema."), os.system("pause")
                return True
                break
    return False

def verificar_run(run):
       
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
        alumno = Alumno()
        run = input("Ingrese el RUN (Formato: 12345678-9): ")

        while verificar_run(run) == False or run_existe(run) == True:
            run = input("Ingrese el RUN (Formato: 12345678-9): ")
        alumno.persona.run = run
        alumno.persona.nombre = input("Ingrese el nombre: ")
        alumno.persona.apellido = input("Ingrese el apellido: ")
        alumno.persona.edad = input("Ingrese la edad: ")
        alumno.persona.asignatura = input("Ingrese la asignatura: ")
        alumno.sesion = int(input("Ingrese la sección: "))
        lista_usuarios.append(alumno)
        print(f"\n Alumno {alumno.persona.nombre} {alumno.persona.apellido} {alumno.persona.run} ingresado exitosamente!")
    elif opcion == "2":
        profesor = Profesor()
        run = input("Ingrese el RUN (Formato: 12345678-9): ")
        while verificar_run(run) == False:
            run = input("Ingrese el RUN (Formato: 12345678-9): ")
        profesor.persona.run = run
        profesor.persona.nombre = input("Ingrese el nombre: ")
        profesor.persona.apellido = input("Ingrese el apellido: ")
        profesor.persona.edad = input("Ingrese la edad: ")
        profesor.persona.asignatura = input("Ingrese la asignatura: ")
        while True:
            sesion = int(input("Ingrese la sección: "))
            if sesion not in profesor.sesion:
                profesor.sesion.append(sesion)
                print(f"\n Sección {sesion} agregada exitosamente!")
            else:
                print(f"\n Sección {sesion} ya existe. Intente nuevamente.")
            respuesta = input("\n ¿Desea agregar otra sección? (si/no): ")
            if respuesta == "no":
                break
            elif respuesta == "si":
                continue
            else:
                respuesta = input("\n Opción no válida. Intente nuevamente. (si/no): ")
        lista_usuarios.append(profesor)
        print(f"\n Profesor {profesor.persona.nombre} {profesor.persona.apellido} ingresado exitosamente!")
    elif opcion == "0":
        return
    else:
        print("\n Opción no válida. Intente nuevamente.")

def verificar_run_profesor(run):
    for usuario in lista_usuarios:
        if usuario.persona.run == run and usuario.rol == "profesor":
            return True
    return False

def ingresar_notas():
    hay_profesor = False
    for usuario in lista_usuarios:
        if usuario.rol == "profesor":
            hay_profesor = True
            break
    
    if hay_profesor == False:
        print(" No hay profesores ingresados, por favor ingrese un profesor")
        os.system("pause")
        return
    
    hay_alumno = False
    for usuario in lista_usuarios:
        if usuario.rol == "alumno":
            hay_alumno = True
            break
    
    if hay_alumno == False:
        print(" No hay alumnos ingresados, por favor ingrese un alumno")
        os.system("pause")
        return
    
    run_profe = input("Ingrese su RUN profesor: ")
    while verificar_run_profesor(run_profe) == False:
        print("\n El profesor no existe. Intente nuevamente.")
        run_profe = input("Ingrese su RUN profesor: ")
    
    run_alumno = input("Ingrese RUN del alumno para agregar notas: ")
    alumno_encontrado = None
    
    for usuario in lista_usuarios:
        if usuario.persona.run == run_alumno and usuario.rol == "alumno":
            alumno_encontrado = usuario
            break
    
    if alumno_encontrado == None:
        print("\n El alumno no existe. Intente nuevamente.")
        return
    
    print(f"\nIngresando notas para: {alumno_encontrado.persona.nombre} {alumno_encontrado.persona.apellido}")
    alumno_encontrado.notas = []
    
    contador = 1
    while contador <= 3:
        nota_texto = input(f"Ingrese la Nota {contador} (1.0 a 7.0): ")
        nota = float(nota_texto)
        if nota >= 1.0 and nota <= 7.0:
            alumno_encontrado.notas.append(nota)
            contador = contador + 1
        else:
            print("La nota debe estar entre 1.0 y 7.0. Intente nuevamente.")
    
    print(f"\n Notas ingresadas exitosamente para {alumno_encontrado.persona.nombre} {alumno_encontrado.persona.apellido}")

def listar_secciones():
    seccion_buscar = int(input("Ingrese la sección a listar: "))
    alumnos_seccion = []
    for usuario in lista_usuarios:
        if usuario.rol == "alumno" and usuario.sesion == seccion_buscar:
            alumnos_seccion.append(usuario)
    if len(alumnos_seccion) == 0:
        print(f"\nNo hay alumnos en la sección {seccion_buscar}")
        return
    print("\n" + "=" * 85)
    print(f"LISTADO DE ALUMNOS - SECCIÓN {seccion_buscar}")
    print("=" * 85)
    print("{:<20} {:>8} {:>8} {:>8} {:>10} {:>18}".format(
        "Nombre", "Nota 1", "Nota 2", "Nota 3", "Promedio", "Estado del Alumno"))
    print("-" * 85)
    
    for alumno in alumnos_seccion:
        nombre_completo = alumno.persona.nombre + " " + alumno.persona.apellido
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
    os.system("pause")


def verificar_run_alumno(run):
    for usuario in lista_usuarios:
        if usuario.persona.run == run and usuario.rol == "alumno":
            return True
    return False

def listar_alumno():
    run = input("Ingrese el RUN del alumno: ")
    while verificar_run_alumno(run) == False:
        print("\n El alumno no existe. Intente nuevamente.") 
        run = input("Ingrese el RUN del alumno: ")   
    for usuario in lista_usuarios:
        if usuario.persona.run == run and usuario.rol == "alumno":
            nombre_completo = usuario.persona.nombre + " " + usuario.persona.apellido
            print("\n" + "=" * 85)
            print(f"Notas del Alumno: {nombre_completo}")
            print("=" * 85)
            print("{:<20} {:>8} {:>8} {:>8} {:>10} {:>18}".format(
                "Nombre", "Nota 1", "Nota 2", "Nota 3", "Promedio", "Estado del Alumno"))
            print("-" * 85)
            if len(usuario.notas) == 3:
                nota1 = usuario.notas[0]
                nota2 = usuario.notas[1]
                nota3 = usuario.notas[2]
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
    os.system("pause")

def listar_profesores():
    run = input("Ingrese el RUN del profesor: ")
    while verificar_run_profesor(run) == False:
        print("\n El profesor no existe. Intente nuevamente.") 
        run = input("Ingrese el RUN del profesor: ")   
    for usuario in lista_usuarios:
        if usuario.persona.run == run and usuario.rol == "profesor":
            profesor_encontrado = usuario
            break
            
    if profesor_encontrado is None:
        print("\n El profesor no existe. Intente nuevamente.")
        os.system("pause")
        return

    nombre_profesor = profesor_encontrado.persona.nombre + " " + profesor_encontrado.persona.apellido
    print("\n" + "=" * 85)
    print(f"Profesor: {nombre_profesor}")
    print(f"Secciones a cargo: {profesor_encontrado.sesion}")
    print("=" * 85)
    
    alumnos_encontrados = []
    for usuario in lista_usuarios:
        if usuario.rol == "alumno" and usuario.sesion in profesor_encontrado.sesion:
            alumnos_encontrados.append(usuario)
    
    if len(alumnos_encontrados) == 0:
        print("\n No hay alumnos registrados en las secciones de este profesor.")
    else:
        print("{:<20} {:<10} {:>8} {:>8} {:>8} {:>10} {:>18}".format(
            "Nombre Alumno", "Sección", "Nota 1", "Nota 2", "Nota 3", "Promedio", "Estado"))
        print("-" * 85)
        
        for alumno in alumnos_encontrados:
            nombre_completo = alumno.persona.nombre + " " + alumno.persona.apellido
            
            if len(alumno.notas) == 3:
                nota1 = alumno.notas[0]
                nota2 = alumno.notas[1]
                nota3 = alumno.notas[2]
                promedio = int((nota1 + nota2 + nota3) / 3 * 10) / 10
                if promedio >= 4.0:
                    estado = "Aprobado"
                else:
                    estado = "Reprobado"
                print("{:<20} {:<10} {:>8.1f} {:>8.1f} {:>8.1f} {:>10.1f} {:>18}".format(
                    nombre_completo, alumno.sesion, nota1, nota2, nota3, promedio, estado))
            else:
                print("{:<20} {:<10} {:>8} {:>8} {:>8} {:>10} {:>18}".format(
                    nombre_completo, alumno.sesion, "S/N", "S/N", "S/N", "S/N", "Sin notas"))
    
    print("=" * 85)
    os.system("pause")

def menu_principal():
    while True:
        print("Menu Principal \n")
        print("1. Ingresar usuarios")
        print("2. Ingresar notas")
        print("3. Listar Secciones")
        print("4. Listar Alumno")
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
            listar_alumno()
        elif opcion == "5":
            listar_profesores()
        elif opcion == "6":
            print("\n¡Hasta luego!")
            break
        else:
            print("\n Opción no válida. Intente nuevamente.")

menu_principal()
