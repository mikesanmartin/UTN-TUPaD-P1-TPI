# Trabajo practico integrador: Análisis de Algoritmos en Python 
# Alumnos: Michel Emmanuel San Martin (mikeemmanuel91@gmail.com)

import time
# Se definen las funciones con el modulo time para ayudarnos a contar en las pruebas empiricas.
def use_time():
    used_time = time.time()
    return used_time

def time_dif(start_time, end_time):
    total_time = end_time - start_time
    print(f"El tiempo transcurrido en la ejecucion fue de: {total_time:.8f} segundos.")

# Algoritmo_1
def buscar_combinacion_bruto(lista, objetivo):
    start = use_time()
    print("Comienzo de Algoritmo_1.")
    objetivo = objetivo.upper()

    for nombre in lista:
        if nombre.upper() == objetivo:
            end=use_time()
            time_dif(start, end)
            print(f"El Pokemon ingresado es el numero #{lista.index(nombre) + 1}")
            return True
    
    else:
        end = use_time()
        time_dif(start, end)
        print("El nombre de pokemon ingresado no es valido o este no pertenece a la region de Kanto.")
        return False

# Algoritmo_2
def busqueda_en_diccionario(lista, objetivo):
    start = use_time()
    print("Comienzo de Algoritmo_2")

    objetivo = objetivo.upper()
    poke_index = {nombre.upper():i + 1 for i, nombre in enumerate(lista)}

    if objetivo in poke_index:
        end = use_time()
        time_dif(start, end)
        print(f"El pokemon ingresado es el numero #{poke_index[objetivo]}")
        return True
    else:
        end = use_time()
        time_dif(start, end)
        print("El nombre del pokemon ingresado no es valido o este no pertenece a la region de Kanto.")
        return False