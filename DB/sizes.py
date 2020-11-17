#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contiene funciones que trabajan la información sobre los tamaños de los sándwiches.

Funciones:
get_sizes -- Obtiene el diccionario de los tamaños de sándwiches.
"""


from os import path
from .reading_files import *
from DB import FOLDER


def get_sizes():
	"""Obtiene un diccionario con los tamaños de sándwiches disponibles junto con sus respectivos precios.
	
	Verifica la existencia del archivo "sandwichsizes.txt" y envía su ruta a BD.reading_files.get_dictionary,
	devolviendo un diccionario con la información leída en dicha función.
	Si no encuentra el archivo, devuelve None.
	"""
	
	file_path = FOLDER / "sandwichsizes.txt"  # Formación de la ruta

	if path.exists(file_path):
		# Donde se guardarán los tamaños
		dict_sizes = get_dictionary(file_path)
		return dict_sizes
