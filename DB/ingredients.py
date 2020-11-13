#!/usr/bin/env python
# -*- coding: utf-8 -*-


from os import path
from . import reading_files
from DB import FOLDER


def get_ingredients():
	"""Obtiene la lista de ingredientes adicionales
	disponibles con sus respectivos precios."""
	
	file_path = FOLDER / "additionalingredients.txt"
	
	if path.exists(file_path):
		# Donde se guardarán los ingredientes
		dict_ingredients = reading_files.get_dictionary(file_path)
		return dict_ingredients
	else:
		print("ingredientes")
