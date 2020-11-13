#!/usr/bin/env python
# -*- coding: utf-8 -*-


from datetime import datetime


def poster():
	"""Cartel de la tienda de sándwiches."""
	
	print("**************************\n"
	      + "*" + "SÁNDWICHES UCAB".center(24) + "*\n"
	      + "**************************\n")


def hello():
	"""Mensaje de entrada al iniciar el programa."""
	poster()
	
	if datetime.now().hour < 12:
		print("Buenos días", end=" ")
	elif datetime.now().hour < 20:
		print("Buenas tardes", end=" ")
	else:
		print("Buenas noches", end=" ")
	
	print("""¡Bienvenid@ a SÁNDWICHES UCAB!
Realice su pedido a continuación...\n""")


def options_list(dict_sizes):
	"""Genera la lista de las opciones disponibles,
	ya sea los tamaños de sándwiches o de los ingredientes extras."""
	
	# Encabezado de la lista
	print("Opción" + "Precio".rjust(30 - len("Opción")) + "Código".rjust(10))
	for i, j in dict_sizes.items():
		print(j[0]  # Nombre
		      + str(j[1]).rjust(30 - len(j[0]))  # Precio
		      + ("( " + i + " )").rjust(10))  # Código del pedido
	print()
	print("Otras opciones:")
	print("Regresar" + "( reg )".rjust(40 - len("Regresar")))
	print()


def sizes_list(dict_sizes):
	"""Muestra el bloque de opciones de tamaños de sándwiches disponibles."""
	
	print("Por favor, elija el tamaño de su sándwich a ordenar.")
	options_list(dict_sizes)


def ingredients_list(dict_sizes):
	"""Muestra el bloque de opciones de ingredientes adicionales disponibles."""
	
	print("¿Desea algún ingrediente extra?")
	options_list(dict_sizes)


def error_ingredients():
	"""Mensaje de error en caso de que
	no se haya encontrado el archivo
	"additionalingredients.txt" o que
	el mismo se encuentre vacío."""
	print("ATENCIÓN: en este momento,"
	      " no contamos con ingredientes"
	      " adicionales.\n"
	      "Lamentamos las molestias")


def error_sizes():
	"""Mensaje de error en caso de que
	no se haya encontrado el archivo
	"sandwichsizes.txt" o que
	el mismo se encuentre vacío."""
	print("ATENCIÓN: en este momento,"
	      " no contamos con ingredientes"
	      " para elaborar nuestros sándwiches.\n"
	      "Lamentamos las molestias")
