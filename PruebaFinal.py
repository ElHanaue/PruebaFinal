import json
import random
import numpy as np

def cargar_datos():
    try:
        with open('trabajadores.json', 'r') as file:
            data = json.load(file)
            trabajadores = np.array(data)
    except FileNotFoundError:
        trabajadores = np.empty((0, 5), dtype=object)
    return trabajadores

def guardar_datos(trabajadores):
    with open('pacientes.json', 'w') as file:
        json.dump(trabajadores.tolist(), file)

def trabajadores():
    listatrabajadores = ['Juan', 'Maria', 'Carlos', 'Ana', 'Pedro', 'Laura', 'Miguel', 'Isabel', 'Francisco', 'Elena']
    return random.choice(listatrabajadores)

def sueldo_aleatorio():
    trabajador = trabajadores(),
    return random.choice(trabajador)

while True:

    print("    --Analisis de datos--");
    print("1. Asignar sueldos aleatorios.");
    print("2. Clasificar Sueldos.");
    print("3. Ver Estadisticas.");
    print("4. Reporte de sueldos.");
    print("5. Salir del programa.");
    
    opcion = input("Ingrese el número de la opción deseada (1-5): ")

    if opcion == '1':
        sueldoaleatorio=random.randint(300000,2500000)
        print(f"Trabajador :{trabajadores}. sueldo generado{sueldoaleatorio}")

    elif opcion == '2':
         print("Clasificacion de sueldo")
    elif opcion == '3':
         print("Estadisticas")
    elif opcion == '4':
         print("Reporte De Sueldos")
    elif opcion == '5':
         print("Finalizando programa...")
         print("Desarrollado por Pedro Leiva")
         print("Rut 18.999.284-k")
        