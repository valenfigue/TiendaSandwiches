#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contiene funciones con todos los mensajes mostrados al usuario durante el flujo del programa.

Funciones:
poster -- Cartel de la tienda de sándwiches.
welcome -- Mensaje de bienvenida.
options_list -- Lista de opciones disponibles (tamaños e ingredientes adicionales).
sizes_list -- Bloque de opciones de tamaños de sándwiches disponibles.
ingredients_list -- Bloque de opciones de ingredientes adicionales disponibles.
error_ingredients -- Mensaje de error por falta de archivo "additionalingredients.txt".
error_sizes -- Mensaje de error por falta de archivo "sandwichsizes.txt".
sub_total -- Resumen de la orden.
total -- Resumen del pedido.
"""


from datetime import datetime


def poster():
	"""Muestra el cartel de la tienda."""
	
	print("**************************\n"
	      + "*" + "SÁNDWICHES UCAB".center(24) + "*\n"
	      + "**************************\n")


def welcome():
	"""Mensaje de entrada al iniciar el programa."""
	poster()
	
	# Cambio de saludo según etapa del día.
	if datetime.now().hour < 12:
		print("Buenos días", end=" ")
	elif datetime.now().hour < 20:
		print("Buenas tardes", end=" ")
	else:
		print("Buenas noches", end=" ")
	
	print("""¡Bienvenid@ a SÁNDWICHES UCAB!
Realice su pedido a continuación...""")


def options_list(dict_options: dict):
	"""Lista de opciones disponibles para el usuario.
	
	Muestra la lista de los tamaños de sándwiches o de los ingredientes extras, según el argumento usado.
	Argumentos:
	dict_options -- Diccionario de ingredientes disponibles: los tamaños del sándwich o los ingredientes adicionales.
	"""
	
	print("Opción" + "Precio".rjust(30 - len("Opción")) + "Código".rjust(10))  # Encabezado de la lista
	# Generación de la lista por pantalla.
	for i, j in dict_options.items():
		print(j["name"]  # Nombre
		      + str(j["price"]).rjust(30 - len(j["name"]))  # Precio
		      + ("( " + i + " )").rjust(10))  # Código del pedido
	print()  # Separación del bloque de respuesta del usuario.


def sizes_list(dict_sizes: dict):
	"""Muestra el bloque de opciones de tamaños de sándwiches disponibles.
	
	Argumentos:
	dict_sizes -- Diccionario de tamaños.
	"""
	
	print()  # Separación del bloque anterior.
	print("Por favor, elija el tamaño de su sándwich a ordenar.")  # Encabezado del bloque.
	options_list(dict_sizes)  # Generación de la lista por pantalla.


def ingredients_list(dict_ingredients: dict):
	"""Muestra el bloque de opciones de ingredientes adicionales disponibles.
	
	Argumentos:
	dict_ingredients -- Diccionario de ingredientes.
	"""
	
	print()  # Separación del bloque anterior.
	print("¿Desea algún ingrediente extra?")  # Encabezado del bloque.
	options_list(dict_ingredients)  # Generación de la lista por pantalla.
	print("Otras opciones:")  # Encabezado de otras opciones.
	print("Cancelar último ingrediente"
	      + "( reg )".rjust(50 - len("Cancelar último ingrediente")))
	print("Cancelar todos los ingredientes extras"
	      + "( can )".rjust(50
	                        - len("Cancelar todos los ingredientes extras")))
	print()  # Separación del bloque de respuesta del usuario.


def error_ingredients():
	"""Mensaje de error en caso de falta del archivo "additionalingredients.txt" o que el mismo se encuentre vacío."""
	print("ATENCIÓN: en este momento,"
	      " no contamos con ingredientes"
	      " adicionales.\n"
	      "Lamentamos las molestias")


def error_sizes():
	"""Mensaje de error en caso de falta del archivo "sandwichsizes.txt" o que el mismo se encuentre vacío."""
	print("ATENCIÓN: en este momento,"
	      " no contamos con ingredientes"
	      " para elaborar nuestros sándwiches.\n"
	      "Lamentamos las molestias")


def sub_total(order: str, sandwich: str, amount: int):
	"""Muestra el resumen de la orden con su subtotal y los ingredientes adicionales pedidos por el usuario.
	
	Argumentos:
	order -- Cadena con la orden completa, incluyendo el tamaño del sándwich y los ingredientes adicionales.
	sandwich -- Nombre del tamaño del sándwich.
	amount -- Monto generado por esta orden.
	"""
	
	print()
	print("Usted seleccionó un sándwich", order)
	print()
	print("Subtotal a pagar por un sándwich " + sandwich
	      + ": " + str(amount))
	print("****************************")


def order_list(order: dict):
	"""Muestra el detalle final de las órdenes de usuario.

	Argumentos:
	:argument order -- Diccionario con el pedido completo del usuario.
	"""
	
	print("\nÓrdenes:")
	print("N°  " + "Detalles".center(25))  # Encabezado de la lista
	# Generación de la lista por pantalla.
	for n_order, sub_order in order.items():
		print(str(n_order).ljust(4) + "Sándwich ", end="")
		print(sub_order["size"]["name"] + " con Queso", end="")  # Nombre
		
		for n_ing, ingrediente in sub_order["ing"].items():
			if ingrediente:  # Solo si hay ingredientes adicionales.
				if n_ing == max(list(sub_order["ing"])):  # Solo para estética del mensaje.
					print(" y", end=" ")
				else:
					print(",", end=" ")
				print(ingrediente.get("name"), end="")
		print("\n\t" + "Subtotal:  ", sub_order["sub_total"])
	print()  # Separación del bloque de respuesta del usuario.
