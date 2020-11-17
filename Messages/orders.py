#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contiene funciones que realizan todos los cálculos referentes a las órdenes tomadas al usuario.

Funciones:
size_order -- Maneja la elección del tamaño del sándwich.
ingredients_order -- Maneja la elección de ingredientes adicionales.
subtotal -- Resumen de la orden.
canceled_order -- Maneja la cancelación de una orden por el usuario.
"""


from . import msg


def size_order(dict_sizes: dict):
	"""Maneja la elección del tamaño del sándwich.
	
	Devuelve el elemento, dentro del diccionario de tamaños, elegido por el usuario.
	Argumentos:
	dict_sizes -- Diccionario con todos los tamaños de sándwiches disponibles.
	"""
	
	# Se muestran las opciones de tamaños de sandwiches
	msg.sizes_list(dict_sizes)
	
	# Proceso de elección
	while True:
		confirmation = '.'
		election = input("Opción a elegir: ").lower()
		
		if election in list(dict_sizes):
			# Muestra, al usuario, la opción que escogió.
			print("Tamaño solicitado:", dict_sizes.get(election)["name"])
			
			# Confirmación del pedido:
			while True:
				confirmation = input("Presione <ENTER> para continuar,"
				                     " o escriba 'cancelar'"
				                     " para elegir otra"
				                     " opción: ")
				if confirmation == 'cancelar' or confirmation == '':
					break
				else:
					print("¡¡Debe confirmar o cancelar su elección!!")
		else:
			print("¡¡Debe elegir el tamaño correcto!!")
		# Opción confirmada. Continúa...
		if confirmation == '':
			break
	return dict_sizes.get(election)


def ingredients_order(dict_ingredients: dict):
	"""Maneja la elección de ingredientes adicionales.
	
	Genera un diccionario con todos los ingredientes adicionales seleccionados por el usuario, para esta orden.
	Argumentos:
	dict_ingredients -- Diccionario con todos los ingredientes adicionales disponibles junto con sus precios.
	"""
	
	# Diccionario que guardará los ingredientes seleccionados.
	order = {1: dict()}  # Visualización del directorio
	n_order = max(list(order))  # Número de orden de ingredientes adicionales

	# Se muestran los ingredientes adicionales disponibles.
	msg.ingredients_list(dict_ingredients)
	
	# Proceso de elección de ingredientes adicionales
	while True:
		election = input("Indique ingrediente"
		                 " (<ENTER> para terminar): ").rstrip().lower()
		
		if election in list(dict_ingredients):
			# Orden agregada
			order.update({n_order: dict_ingredients.get(election)})
			# Aumenta el número de orden de ingredientes adicionales
			n_order += 1
		else:
			if n_order > 1:
				# Eliminar el ingrediente anterior
				if election == 'reg':
					del order[n_order - 1]
					n_order -= 1
					print("ATENCIÓN: último ingrediente"
					      " eliminado de la orden.")
					continue
				# Eliminar todos los ingredientes seleccionados
				elif election == 'can':
					order.clear()
					print("ATENCIÓN: todos los ingredientes"
					      " eliminados de la orden")
					n_order = 1
					continue
			if election == '':  # Terminar
				break
			else:
				print("¡¡Debe elegir el ingrediente adicional correcto!!")
	return order


def subtotal(sub_order: dict):
	"""Resumen de la orden.
	
	Calcula y muestra el subtotal a pagar por una orden en específico, y lo retorna junto con la confirmación de
	siguiente orden.
	Argumentos:
	sub_order -- Diccionario con la orden actual.
	"""
	
	sandwich = sub_order.get("size").get("name")
	order = sandwich + " con Queso"
	amount = sub_order.get("size").get("price")
	
	# Cálculo del subtotal de la orden.
	for i, j in sub_order["ing"].items():
		if j:
			if i == max(list(sub_order["ing"])):  # Solo para estética del mensaje.
				order += " y "
			else:
				order += ", "
			
			order += j.get("name")  # Orden actual.
			amount += j.get("price")  # Sub total de la orden.
	msg.sub_total(order, sandwich, amount)  # Mensaje
	while True:  # Confirmación
		print("¿Desea continuar? [s/n]")
		print("Si desea cancelar toda la orden"
		      " de este sándwich, ingrese 'can'.")
		confirmation = input("Respuesta: ").rstrip().lower()
		
		if confirmation == 's' or confirmation == 'n' or confirmation == 'can':
			break
		else:
			print("¡¡Respuesta inválida!!")
	return confirmation, amount


def canceled_order(n_order: int, order: dict):
	"""Mensaje de cancelación de la orden y retorno de confirmación para realizar otra, reiniciando el ciclo.
	
	Es activada cuando el usuario indica la cancelación de la orden actual en el resumen del subtotal de la misma.
	Muestra el mensaje de orden cancelada y elimina la misma del diccionario de órdenes.
	
	Argumentos:
	n_orden -- Número de la orden a cancelar.
	order -- Diccionario de todas las órdenes.
	"""
	
	print("ATENCIÓN: ¡¡Orden", n_order, "cancelada!!")
	order.pop(n_order)  # Se elimina la orden cancelada.
	
	return 's'  # Para que "next_order" permita volver a realizar el ciclo.
