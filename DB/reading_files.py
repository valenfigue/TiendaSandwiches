#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Valentina Figueroa <valenfiguer14@gmail.com>
"""Contiene funciones encargadas de la lectura y escritura de archivos de texto usados para este programa.

Funciones:
- `get_dictionary(file)`: Obtiene la información de tamaños e ingredientes adicionales de los sándwiches.
"""


from os import path


def get_dictionary(file: str):
	"""Retorna un diccionario con código, nombre y precio del ingrediente leído desde el archivo.
	
	Verifica la existencia del archivo del argumento de la función, lo lee y genera un diccionario con el código,
	nombre y precio del ingrediente	obtenido del texto. Si no encuentra el archivo, devuelve None.
	
	:argument file: ruta del archivo a leer.
	"""
	if path.exists(file):
		dictionary = dict()  # Donde se guardará el contenido.
		
		f = open(file, 'r', encoding='utf-8')  # Abre el archivo para leerlo.
		
		# Esto es para saltar las líneas de codificación de cada archivo .txt
		f.readline()
		f.readline()
		
		f.readline()  # Esto es para saltar la línea que identifica el autor del proyecto.
		
		while True:  # Lectura de archivo
			key = f.readline().rstrip().lower()  # Obteniendo la clave.
			
			if not key:  # Si no hay más líneas, rompe el ciclo.
				break
			name = f.readline().rstrip().capitalize()  # Obteniendo el nombre del ingrediente.
			price = float(f.readline().rstrip())  # Obteniendo su precio.
			
			# Guardando la clave, el nombre y el precio, en un diccionario
			dictionary.update({key: {"name": name, "price": price}})
		f.close()  # Cierra la lectura del archivo.
	
		return dictionary
