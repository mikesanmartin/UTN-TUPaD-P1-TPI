# Trabajo practico integrador: Análisis de Algoritmos en Python 
# Alumnos: 
# Michel Emmanuel San Martin (mikeemmanuel91@gmail.com)
# Brian Santaran (brian.santaran@tupad.utn.edu.ar) 

from lista_pokemon import lista
from lista_pokemon_completa import lista_completa
import algoritmos_tpi

poke_busqueda = input("Por favor, ingrese el nombre de un pokemon: ")

algoritmos_tpi.buscar_combinacion_bruto(lista_completa, poke_busqueda)

algoritmos_tpi.busqueda_en_diccionario(lista_completa, poke_busqueda)