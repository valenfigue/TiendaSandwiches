#!/usr/bin/env python
# -*- coding: utf-8 -*-


from os import path
from .reading_files import *
from DB import FOLDER


def get_sizes():
	
	"""Obtiene la lista de tamaños de sándwiches
	disponibles con sus respectivos precios."""
	
	file_path = FOLDER / "sandwichsizes.txt"

	if path.exists(file_path):
		# Donde se guardarán los tamaños
		dict_sizes = get_dictionary(file_path)
		return dict_sizes
