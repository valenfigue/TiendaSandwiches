from os import path
from .reading_files import *
from DB import FOLDER


def get_ingredients():
	"""Obtiene la lista de ingredientes adicionales
	disponibles con sus respectivos precios."""
	
	file_path = FOLDER / "additionalingredients.txt"
	
	if path.exists(file_path):
		# Donde se guardarán los ingredientes
		dict_ingredients = get_dictionary(file_path)
		return dict_ingredients
	else:
		print("ingredientes")
