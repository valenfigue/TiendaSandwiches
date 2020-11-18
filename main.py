#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contiene una función para ejecutar la Tienda de Sándwiches UCAB."""

from DB import sizes
from DB import ingredients as ing
from Messages import orders, msg


def tienda():
	"""Función principal del programa."""
	
	# Ingredientes para hacer los sándwiches.
	dict_sizes = sizes.get_sizes()  # Tamaños.
	dict_ing = ing.get_ingredients()  # Ingredientes adicionales.
	
	# Directorio que guarda toda la información de cada orden del pedido.
	# Contiene: Número de orden. Para cada orden:
	# Visualización del directorio.
	order = {1: {  # Número de la orden
		"size": dict(),  # El tamaño del sándwich y su precio.
		"ing": {1: dict()},  # Los ingredientes adicionales y el precio de cada uno.
		"sub_total": 0}}  # El sub total de la orden.
	
	n_order = 1  # Número de orden del usuario.
	next_order = 's'  # Confirmación para realizar la siguiente orden de sándwich
	
	msg.welcome()  # Mensaje de bienvenida.
	
	if dict_sizes:  # En caso de que no encuentre el archivo "sandwichsizes.txt" o este esté vacío.
		if not dict_ing:  # En caso de que no encuentre el archivo "additionalingredients.txt" o este esté vacío.
			msg.error_ingredients()
		
		while next_order == 's':  # Mientras que se quiera otra orden...
			print("\n\nSándwich número", n_order)
			
			# Pregunta sobre el tamaño de sándwich.
			order.update({n_order: {"size": orders.size_order(dict_sizes)}})
			
			# Pregunta sobre los ingredientes adicionales.
			if dict_ing:  # Solo si encontró el archivo "additionalingredients.txt"
				order[n_order].update({"ing": orders.ingredients_order(dict_ing)})
			else:  # En caso de que no encuentre el archivo
				# "additionalingredients.txt" o este esté vacío.
				order[n_order].update({"ing": {}})
			
			# Cálculo del subtotal de la orden y confirmación de siguiente orden.
			next_order = orders.subtotal(order.get(n_order))
			
			# Cálculo del total del pedido.
			if next_order == 'n':  # Ya no se desea realizar más órdenes...
				msg.total(order)  # Resumen del pedido.
			elif next_order == 'can':  # Cancelar la orden actual
				next_order = orders.canceled_order(n_order, order)  # Cancelación de la orden.
			else:  # Número de siguiente orden.
				n_order += 1
	else:
		msg.error_sizes()


if __name__ == "__main__":
	tienda()
