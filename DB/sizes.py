#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Valentina Figueroa <valenfiguer14@gmail.com>
"""Contiene funciones que trabajan la información sobre los tamaños de los sándwiches.

Funciones:
- `get_sizes()`: Obtiene el diccionario de los tamaños de sándwiches.
"""


from .reading_files import *
from DB import FOLDER, resolver_ruta


def get_sizes():
	"""Obtiene un diccionario con los tamaños de sándwiches disponibles junto con sus respectivos precios.
	
	Envía la ruta del archivo "sandwichsizes.txt" a BD.reading_files.get_dictionary, devolviendo un
	diccionario con la información leída en dicha función.
	"""
	
	file = "sandwichsizes.txt"
	file_path = FOLDER / file  # Formación de la ruta
	resolved_file_path = resolver_ruta(file_path)  # Resolución de la ruta para el ejecutable.

	return get_dictionary(resolved_file_path)
