from lista_pokemon import lista
from lista_pokemon_completa import lista_completa
import algoritmos_tpi

poke_busqueda = input("Por favor, ingrese el nombre de un pokemon: ")

algoritmos_tpi.buscar_combinacion_bruto(lista_completa, poke_busqueda)

algoritmos_tpi.busqueda_en_diccionario(lista_completa, poke_busqueda)