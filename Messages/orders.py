#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Módulo en donde se realizan todos los cálculos referentes
a las órdenes tomadas al usuario."""


from . import msg


def size_order(dict_sizes):
	"""Maneja la elección del tamaño del sándwich."""
	
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
				confirmation = input("Presione <ENTER> para continuar, "
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


def ingredients_order(dict_ingredients):
	"""Maneja la elección de ingredientes adicionales."""
	
	# Diccionario que guardará los ingredientes seleccionados.
	order = {1: dict()}
	n_order = max(list(order))  # Número de orden de ingredientes adicionales

	# Se muestran los ingredientes adicionales disponibles.
	msg.ingredients_list(dict_ingredients)
	
	# Proceso de elección de ingredientes adicionales
	while True:
		election = input("Indique ingrediente"
		                 " (<ENTER> para terminar): ").lower()
		
		if election in list(dict_ingredients):
			# Orden agregada
			order[n_order] = dict_ingredients.get(election)
			# Aumenta el número de orden de ingredientes adicionales
			n_order += 1
		# elif election == 'reg':
		elif election == '':
			break
		else:
			print("¡¡Debe elegir el ingrediente adicional correcto!!")
	return order


def subtotal(sub_order):
	"""Calcula y muestra el subtotal a pagar por una orden
	en específico."""
	
	sandwich = sub_order.get("size").get("name")
	order = sandwich + " con Queso"
	amount = sub_order.get("size").get("price")
	
	# Cálculo del subtotal de la orden
	for i, j in sub_order["ing"].items():
		if j:
			if i == max(list(sub_order["ing"])):
				order += " y "
			else:
				order += ", "
			
			order += j.get("name")
			amount += j.get("price")
	# Mensaje
	msg.sub_total(order, sandwich, amount)
	while True:
		confirmation = input("¿Desea continuar? [s/n]: ").rstrip().lower()
		
		if confirmation == 's' or confirmation == 'n':
			break
		else:
			print("¡¡Respuesta inválida!!")
			continue
	return confirmation, amount


def total(n_sandwiches, amount):
	"""Muestra el total de sándwiches pedidos y el precio
	a pagar por todos ellos."""
	
	print("El pedido tiene un total de", n_sandwiches,
	      ("sándwich" if n_sandwiches == 1 else "sándwiches") + ",",
	      "por un monto de", amount)
	
	print("\nGracias por su compra ¡Vuelva pronto!")