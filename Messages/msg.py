#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Valentina Figueroa <valenfiguer14@gmail.com>
"""Contiene funciones con todos los mensajes solamente mostrados al usuario durante el flujo del programa.

Funciones:

- `poster()`: Cartel de la tienda de sándwiches.
- `number_sandwich(n_order)`: Número de orden a tomar.
- `welcome()`: Mensaje de bienvenida.
- `options_list(dict_options)`: Lista de opciones disponibles (tamaños e ingredientes adicionales).
- `sizes_list(dict_sizes)`: Bloque de opciones de tamaños de sándwiches disponibles.
- `ingredients_list(dict_ingredients)`: Bloque de opciones de ingredientes adicionales disponibles.
- `error_ingredients()`: Mensaje de error por falta de archivo "additionalingredients.txt".
- `error_sizes()`: Mensaje de error por falta de archivo "sandwichsizes.txt".
- `sub_total(order, sandwich, amount)`: Resumen de la orden.
- `total` Resumen del pedido.
- `order_list(order)`: Detalle final del pedido completo.
"""


from datetime import datetime
from . import voices, y_or_comma


def poster():
	"""Muestra el cartel de la tienda."""
	
	print("**************************\n"
	      + "*" + "SÁNDWICHES UCAB".center(24) + "*\n"
	      + "**************************\n")


def welcome():
	"""Mensaje de entrada al iniciar el programa."""
	
	poster()
	
	# Cambio de saludo según etapa del día.
	if 5 <= datetime.now().hour < 12:
		print("Buenos días", end=" ")
	elif 12 <= datetime.now().hour < 20:
		print("Buenas tardes", end=" ")
	else:
		print("Buenas noches", end=" ")
	
	print("""¡Bienvenid@ a SÁNDWICHES UCAB!
Realice su pedido a continuación...""")
	voices.welcome_voice()


def number_sandwich(n_order: int):
	"""Número de sándwich a ordenar.
	
	:argument n_order: número de orden.
	"""
	
	print("\n\nSándwich número", n_order)
	voices.number_sandwich_voice(str(n_order))


def options_list(dict_options: dict):
	"""Lista de opciones disponibles para el usuario.
	
	Muestra la lista de los tamaños de sándwiches o de los ingredientes extras, según el argumento usado.
	
	:argument dict_options: Diccionario de ingredientes disponibles: los tamaños o los ingredientes adicionales.
	"""
	
	print("Opción" + "Precio".rjust(30 - len("Opción")) + "Código".rjust(10))  # Encabezado de la lista
	# Generación de la lista por pantalla.
	for code, item in dict_options.items():
		print(item["name"]  # Nombre
		      + str(item["price"]).rjust(30 - len(item["name"]))  # Precio
		      + ("( " + code + " )").rjust(10))  # Código del pedido
	print()  # Separación del bloque de respuesta del usuario.


def sizes_list(dict_sizes: dict):
	"""Muestra el bloque de opciones de tamaños de sándwiches disponibles.
	
	:argument dict_sizes: Diccionario de tamaños.
	"""
	
	print()  # Separación del bloque anterior.
	print("Por favor, elija el tamaño del sándwich a ordenar.")  # Encabezado del bloque.
	options_list(dict_sizes)  # Generación de la lista por pantalla.
	voices.sizes_list_voice()


def ingredients_list(dict_ingredients: dict):
	"""Muestra el bloque de opciones de ingredientes adicionales disponibles.
	
	:argument dict_ingredients: Diccionario de ingredientes.
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
	voices.ingredients_list_voice()


def error_ingredients():
	"""Mensaje de error en caso de faltar archivo "additionalingredients.txt" o que el mismo se encuentre vacío."""
	print("ATENCIÓN: en este momento,"
	      " no contamos con ingredientes"
	      " adicionales.\n"
	      "Lamentamos las molestias")


def error_sizes():
	"""Mensaje de error en caso de faltar archivo "sandwichsizes.txt" o que el mismo se encuentre vacío."""
	print("ATENCIÓN: en este momento,"
	      " no contamos con ingredientes"
	      " para elaborar nuestros sándwiches.\n"
	      "Lamentamos las molestias")


def sub_total(order: str, sandwich: str, amount: int):
	"""Muestra el resumen de la orden con su subtotal y los ingredientes adicionales pedidos por el usuario.
	
	:argument order: Cadena con la orden completa, incluyendo el tamaño del sándwich y los ingredientes adicionales.
	:argument sandwich: Nombre del tamaño del sándwich.
	:argument amount: Monto generado por esta orden.
	"""
	
	print()
	print("Usted seleccionó un sándwich", order)
	print()
	print("Subtotal a pagar por un sándwich " + sandwich
	      + ": " + str(amount))
	print("****************************")
	voices.sub_total_voice(order)


def order_list(order: dict):
	"""Muestra el detalle final de las órdenes de usuario.

	:argument order: Diccionario con el pedido completo del usuario.
	"""
	
	print("\n\nRESUMEN DEL PEDIDO:".center(34))
	print("N°  " + "Orden".center(30))  # Encabezado de la lista.
	
	for n_order, sub_order in order.items():  # Generación de la lista por pantalla.
		print(str(n_order).ljust(4) + "Sándwich ", end="")
		print(sub_order["size"]["name"] + " con Queso", end="")  # Tamaño.
		
		for n_ing, ingredient in sub_order["ing"].items():  # Ingredientes adicionales.
			print(str(y_or_comma(n_ing, sub_order["ing"])), end="")  # Solo por fines estéticos.
			print(ingredient.get("name"), end="")
		print("\n\t" + "Subtotal:  ", sub_order["sub_total"])  # Subtotal de la orden.
