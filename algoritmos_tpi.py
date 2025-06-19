# Trabajo practico integrador: Análisis de Algoritmos en Python 
# Alumnos: Michel Emmanuel San Martin (mikeemmanuel91@gmail.com)

# Algoritmo_1
def dos_numeros_bruto(lista, objetivo):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == objetivo:
                return (lista[i], lista[j])
    return None

# Algoritmo_2
def dos_numeros_hashset(lista, objetivo):
    vistos = set()
    for num in lista:
        complemento = objetivo - num
        if complemento in vistos:
            return (complemento, num)
        vistos.add(num)
    return None