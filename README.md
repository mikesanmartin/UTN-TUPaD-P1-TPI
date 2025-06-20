# UTN-TUPaD-P1-TPI

## Trabajo Práctico Integrador - Programación 1

**Alumnos:**
- Michel Emmanuel San Martin (mikeemmanuel91@gmail.com)
- Brian Santaran (brian.santaran@tupad.utn.edu.ar)

---

## Descripción General

Este repositorio contiene un proyecto de análisis de algoritmos en Python, enfocado en la búsqueda de Pokémon por nombre. El objetivo es comparar la eficiencia de dos métodos de búsqueda (búsqueda secuencial y búsqueda usando diccionario) y analizar sus tiempos de ejecución.

---

## Estructura del Repositorio

- `main.py`: Script principal. Solicita al usuario el nombre de un Pokémon y ejecuta ambos algoritmos de búsqueda, mostrando los resultados y el tiempo de ejecución de cada uno.
- `algoritmos_tpi.py`: Contiene la implementación de los algoritmos de búsqueda y funciones auxiliares para medir el tiempo de ejecución.
- `lista_pokemon.py`: Lista de ejemplo con los primeros 150 Pokémon (región Kanto).
- `lista_pokemon_completa.py`: Lista extendida con más de 1000 Pokémon (todas las generaciones).

---

## Explicación de los Archivos

### `main.py`
- Importa las listas de Pokémon y los algoritmos.
- Solicita al usuario el nombre de un Pokémon por consola.
- Ejecuta ambos algoritmos de búsqueda sobre la lista (`lista`).
- Muestra el resultado y el tiempo de ejecución de cada algoritmo.

### `algoritmos_tpi.py`
- Incluye funciones para medir el tiempo de ejecución (`use_time`, `time_dif`).
- **Algoritmo 1: Búsqueda Bruta** (`buscar_combinacion_bruto`):
  - Recorre la lista secuencialmente y compara el nombre ingresado (ignorando mayúsculas/minúsculas).
  - Si encuentra coincidencia, muestra el número del Pokémon y el tiempo de ejecución.
  - Si no lo encuentra, informa que el nombre no es válido o no se encuentra.
- **Algoritmo 2: Búsqueda con Diccionario** (`busqueda_en_diccionario`):
  - Convierte la lista en un diccionario para acceso rápido por nombre.
  - Busca el nombre ingresado en el diccionario.
  - Muestra el número del Pokémon y el tiempo de ejecución si lo encuentra, o un mensaje de error si no.

### `lista_pokemon.py`
- Contiene una lista llamada `lista` con los primeros 150 Pokémon (región Kanto), utilizada para las pruebas y ejemplos.

### `lista_pokemon_completa.py`
- Contiene una lista llamada `lista_completa` con más de 1000 Pokémon, abarcando todas las generaciones. Permite realizar pruebas de eficiencia con una lista mucho más grande.

---

## ¿Cómo ejecutar el proyecto?

1. Asegúrate de tener Python instalado.
2. Ejecuta el archivo principal:
   ```sh
   python main.py
   ```
3. Ingresa el nombre de un Pokémon cuando se solicite.
4. El programa mostrará los resultados y el tiempo de ejecución de ambos algoritmos.

---

## Ejemplo de Uso

```
Por favor, ingrese el nombre de un pokemon: Pikachu
Comienzo de Algoritmo_1.
El tiempo transcurrido en la ejecucion fue de: 0.00001240 segundos.
El Pokemon ingresado es el numero #25
Comienzo de Algoritmo_2
El tiempo transcurrido en la ejecucion fue de: 0.00000596 segundos.
El pokemon ingresado es el numero #25
```

---

## Notas y Observaciones

- Por defecto, ambos algoritmos utilizan la lista de Kanto (`lista`). Puedes modificar el código en `main.py` para usar la lista completa (`lista_completa`) si deseas comparar el rendimiento con una lista más grande.
- El análisis de tiempos es orientativo y puede variar según el equipo y el sistema operativo.
- El código está pensado para ser didáctico y fácil de entender.

---

## Enlace a Video Explicativo

URL_YT:

---
