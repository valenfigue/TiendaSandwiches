#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contiene funciones encargadas de la lectura y escritura de archivos de texto usados para este programa.

Funciones:
get_dictionary -- Obtiene los diccionarios de tamaños e ingredientes adicionales de los sándwiches, con sus precios.
"""


def get_dictionary(file: str):
	"""Retorna un diccionario con código, nombre y precio del ingrediente leído desde el archivo.
	
	Argumentos:
	file -- ruta del archivo a leer (Tipo esperado: str)
	"""
	
	dictionary = dict()  # Donde se guardará el contenido.
	
	f = open(file, 'r', encoding='utf-8')
	# Esto es para saltar las líneas de codificación de cada archivo .txt
	f.readline()
	f.readline()
	while True:  # Lectura de archivo
		key = f.readline().rstrip().lower()  # Obteniendo la clave.
		
		if not key:  # Si no hay más líneas, rompe el ciclo.
			break
		name = f.readline().rstrip().capitalize()  # Obteniendo el nombre del ingrediente.
		price = float(f.readline().rstrip())  # Obteniendo su precio.
		# Guardando la clave, el nombre y el precio, en un diccionario
		dictionary.update({key: {"name": name, "price": price}})
	f.close()

	return dictionary
