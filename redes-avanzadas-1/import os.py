import os

x = 0
y = 0
os.system("cls")
campus = ["zona core", "campus uno", "campus matriz", "sector outsourcing"]  # Cambiando de tupla a lista
print("¿Qué quiere hacer?")
print("1. Ver los dispositivos.\n2. Ver los campus.\n3. Añadir dispositivo.\n4. Añadir campus.\n5. Borrar dispositivo.\n6. Borrar campus")
selector = int(input("Elija una opción: "))

if selector == 1:
    os.system("cls")
    y = 1
    print("Elija un campus \n")
    while len(campus) >= y:
        for item in campus:
            print(str(y) + ".", item)
            y += 1
    selector = int(input("\n Elija una opción: "))
    x = selector - 1
    if x >= 0:
        os.system("cls")
        file = open(campus[x] + ".txt", "r")
        for item in file:
            item = item.strip()
            print(item)
        file.close()

elif selector == 2:
    os.system("cls")
    y = 1
    for item in campus:
        print(str(y) + ".", item)
        y += 1

elif selector == 3:
    os.system("cls")
    y = 1
    servicios = []
    print("¿Dónde agregar nuevo dispositivo? \n")
    while len(campus) >= y:
        for item in campus:
            print(str(y) + ".", item)
            y += 1
    selector = int(input("\n Elija una opción: "))
    x = selector - 1
    if x >= 0:
        os.system("cls")
        file = open(campus[x] + ".txt", "a")
        print("Elija un dispositivo: \n \n1. Router. \n2. Switch. \n3. Switch multicapa. \n")
        variable1 = int(input("Elija su opción: "))
        os.system("cls")
        print("Agregue el nombre de su dispositivo")
        variable2 = input("Agregue su nombre: ")
        while True:
            print("¿Confirma este nombre? \n \n1. Si \n2. No \n")
            variable3 = input("Introduzca su respuesta: ")
            if variable3 == "1":
                print("Terminado")
                break
        print("Elija una jerarquía: \n \n1. Núcleo, \n2. Acceso. \n3. Distribución. \n")
        variable3 = input("Elija una opción: ")
        os.system("cls")
        file.write("\n---------------------------------\n")
        if variable1 == 1:
            print("Elija un servicio de red para el router: \n1. Enrutamiento \n2. Salir")
            variable4 = int()
            while variable4 != 2:
                variable4 = int(input("Elija una opción: "))
                if variable4 == 1:
                    servicios.append("Datos")
        file.write("Router: " + variable2)
        if int(variable3) == 1:
            file.write("\nJerarquía: Núcleo")
        elif int(variable3) == 2:
            file.write("\nJerarquía: Distribución")
        elif int(variable3) == 3:
            file.write("\nJerarquía: Acceso")
        file.write("\nServicio: " + str(servicios))
        file.write("\n---------------------------------\n")
        file.close()

elif selector == 4:
    os.system("cls")
    nuevo_campus = input("Ingrese el nombre del nuevo campus: ")
    campus.append(nuevo_campus)
    with open(nuevo_campus + ".txt", "w") as file:
        file.write("Archivo para el campus: " + nuevo_campus)
    print("Nuevo campus añadido con éxito.")
elif selector == 5:
    def borrar_dispositivo(campus):
     print("Elija un campus para borrar un dispositivo \n")
    for item in campus:
        print(str(y) + ".", item)
        y += 1
    selector = int(input("\n Elija una opción: "))
    x = selector - 1
    if x >= 0:
        os.system("cls")
        print("Dispositivos disponibles en", campus[x], "\n")
        file = open(campus[x] + ".txt", "r")
        dispositivos = []
        for item in file:
            item = item.strip()
            dispositivos.append(item)
            print(len(dispositivos), ".", item)
        file.close()
        if len(dispositivos) > 0:
            opcion_borrar = int(input("\n Elija el número del dispositivo que desea borrar: "))
            if opcion_borrar >= 1 and opcion_borrar <= len(dispositivos):
                dispositivo_a_borrar = dispositivos[opcion_borrar - 1]
                with open(campus[x] + ".txt", "w") as file:
                    for dispositivo in dispositivos:
                        if dispositivo != dispositivo_a_borrar:
                            file.write(dispositivo + "\n")
                print("El dispositivo", dispositivo_a_borrar, "ha sido borrado exitosamente.")
            else:
                print("Opción inválida.")
        else:
            print("No hay dispositivos para borrar en", campus[x])

elif selector == 6:
    def borrar_campus(campus):
        print("Elija un campus para borrar: \n")
    for index, item in enumerate(campus, start=1):
        print(f"{index}. {item}")
        selector = int(input("\n Elija una opción: "))
        x = selector - 1
        if x >= 0:
            os.system("cls")
            campus_a_borrar = campus[x]
        # Eliminar el campus de la lista
        del campus[x]
        # Eliminar el archivo correspondiente al campus
        try:
            os.remove(campus_a_borrar + ".txt")
            print("El campus", campus_a_borrar, "y todos sus dispositivos han sido borrados exitosamente.")
        except FileNotFoundError:
            print("No se encontró el archivo del campus", campus_a_borrar)
        except Exception as e:
            print("Ocurrió un error al borrar el campus:", str(e))
