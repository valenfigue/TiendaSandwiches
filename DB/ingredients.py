#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Valentina Figueroa <valenfiguer14@gmail.com>
"""Contiene funciones que trabajan la información sobre los ingredientes adicionales para los sándwiches.

Funciones:
- `get_ingredients()`: Obtiene el diccionario de los ingredientes adicionales.
"""


from os import path
from .reading_files import *
from DB import FOLDER


def get_ingredients():
	"""Obtiene un diccionario con los ingredientes adicionales disponibles junto con sus respectivos precios.
	
	Verifica la existencia del archivo "additionalingredients.txt" y envía su ruta a BD.reading_files.get_dictionary,
	devolviendo un diccionario con la información leída en dicha función. Si no encuentra el archivo, devuelve None.
	"""
	
	file_path = FOLDER / "additionalingredients.txt"  # Formación de la ruta
	
	if path.exists(file_path):
		dict_ingredients = get_dictionary(file_path)  # Donde se guardarán los ingredientes
		return dict_ingredients
