#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Valentina Figueroa <valenfiguer14@gmail.com>
"""Contiene funciones que realizan todos los cálculos referentes a las órdenes tomadas al usuario.

Funciones:
- `size_order(dict_sizes)`: Maneja la elección del tamaño del sándwich.
- `ingredients_order(dict_ingredients)`: Maneja la elección de ingredientes adicionales.
- `subtotal(sub_order)`: Resumen de la orden.
- `canceled_order(n_order, order)`: Maneja la cancelación de una orden por el usuario.
- `total(order)`: resumen final del pedido.
- ``:
"""

from . import msg, voices, y_or_comma


def size_order(dict_sizes: dict) -> dict:
	"""Maneja la elección del tamaño del sándwich.
	
	Devuelve el elemento, dentro del diccionario de tamaños, elegido por el usuario.
	
	:argument dict_sizes: Diccionario con todos los tamaños de sándwiches disponibles.
	"""
	
	# Se muestran las opciones de tamaños de sandwiches
	msg.sizes_list(dict_sizes)
	
	while True:  # Proceso de elección
		confirmation = '.'  # Inicialización de variable.
		election = input("Opción a elegir: ").lower()
		
		if election in list(dict_sizes):
			# Muestra, al usuario, la opción que escogió.
			print("Tamaño solicitado:", dict_sizes.get(election)["name"])
			voices.selected_size_voice(dict_sizes.get(election)["name"])
			
			voices.confirmation_voice()
			while True:  # Confirmación del pedido:
				confirmation = input("Presione <ENTER> para continuar,"
				                     " o escriba 'can'"
				                     " para elegir otra"
				                     " opción: ").rstrip()
				if confirmation == 'can' or confirmation == '':  # Opción correcta.
					break
				else:
					voices.wrong_answer_voice()
					print("¡¡Debe confirmar o cancelar su elección!!")
		else:
			voices.wrong_answer_voice()
			print("¡¡Debe elegir el tamaño correcto!!")
		if confirmation == '':  # Opción confirmada. Continúa...
			break
	return dict_sizes.get(election)


def ingredients_order(dict_ingredients: dict) -> dict:
	"""Maneja la elección de ingredientes adicionales.
	
	Genera un diccionario con todos los ingredientes adicionales seleccionados por el usuario, para esta orden.
	
	:argument dict_ingredients: Diccionario con todos los ingredientes adicionales disponibles junto con sus precios.
	"""
	
	# Visualización del diccionario que guardará los ingredientes seleccionados.
	order = {1: {  # Número del ingrediente.
		"name": str(),  # Nombre del ingrediente seleccionado.
		"price": 0}}  # Precio del ingrediente seleccionado.
	n_order = 1  # Clave del número de ingrediente adicional de la orden actual.

	# Se muestran los ingredientes adicionales disponibles.
	msg.ingredients_list(dict_ingredients)
	
	# Proceso de elección de ingredientes adicionales
	while True:
		election = input("Indique ingrediente"
		                 " (<ENTER> para terminar): ").rstrip().lower()
		
		if election in list(dict_ingredients):
			order.update({n_order: dict_ingredients.get(election)})  # Orden agregada
			n_order += 1  # Aumenta el número de orden de ingredientes adicionales
		else:
			if n_order > 1:  # Para evitar error la introducir opción extra ('reg' o 'can'), cuando no hay
				# ingredientes adicionados a la orden, aun.
				
				if election == 'reg':  # Eliminar el ingrediente anterior
					del order[n_order - 1]
					n_order -= 1
					print("ATENCIÓN: último ingrediente"
					      " eliminado de la orden.")
					voices.canceled_ingredients_voice(election)
					continue
					
				elif election == 'can':  # Eliminar todos los ingredientes seleccionados
					order.clear()
					print("ATENCIÓN: todos los ingredientes"
					      " eliminados de la orden")
					n_order = 1
					voices.canceled_ingredients_voice(election)
					continue
			if election == '':  # Terminar
				break
			else:
				voices.wrong_answer_voice()
				print("¡¡Debe elegir el ingrediente adicional correcto!!")
	return order


def subtotal(sub_order: dict) -> str:
	"""Resumen de la orden.
	
	Calcula y muestra el subtotal a pagar por una orden en específico, actualizando el diccionario del pedido.
	Además, retorna la confirmación de siguiente orden.
	
	:argument sub_order: Diccionario con la orden actual.
	"""
	
	sandwich = sub_order.get("size").get("name")
	order = sandwich + " con Queso"
	amount = sub_order.get("size").get("price")
	
	# Cálculo del subtotal de la orden.
	for n_ing, ingredient in sub_order["ing"].items():
		order += str(y_or_comma(n_ing, sub_order["ing"]))  # Solo por fines estéticos.
		
		order += ingredient.get("name")  # Orden actual.
		amount += ingredient.get("price")  # Sub total de la orden.
	msg.sub_total(order, sandwich, amount)  # Resumen de la orden.
	
	while True:  # Confirmación
		print("¿Desea continuar? [s/n]")
		voices.next_order_voice()
		print("Si desea cancelar toda la orden"
		      " de este sándwich, ingrese 'can'.")
		confirmation = input("Respuesta: ").rstrip().lower()
		
		if confirmation == 's' or confirmation == 'n' or confirmation == 'can':
			break
		else:
			print("¡¡Respuesta inválida!!")
			voices.wrong_answer_voice()
	sub_order.update({"sub_total": amount})
	
	return confirmation


def canceled_order(n_order: int, order: dict) -> str:
	"""Mensaje de cancelación de la orden y retorno de confirmación para realizar otra, reiniciando el ciclo.
	
	Es activada cuando el usuario indica la cancelación de la orden actual en el resumen del subtotal de la misma.
	Muestra el mensaje de orden cancelada y elimina la misma del diccionario de pedido.
	
	:argument n_order: Número de la orden a cancelar.
	:argument order: Diccionario de todas las órdenes.
	"""
	
	print("ATENCIÓN: ¡¡Orden", n_order, "cancelada!!")
	voices.canceled_order_voice(str(n_order))
	order.pop(n_order)  # Se elimina la orden cancelada.
	
	return 's'  # Para que "next_order" permita volver a realizar el ciclo.


def total(order: dict):
	"""Muestra el resumen del pedido, con el total de sándwiches y el precio a pagar por todos ellos.

	:argument order: Pedido o diccionario con todas las órdenes del usuario.
	"""
	n_sandwiches = max(list(order))  # Número de sándwiches pedidos.
	amount = 0
	for n_order in order:
		amount += order[n_order].get("sub_total")
		
	msg.order_list(order)
	print("\nEl pedido tiene un total de", n_sandwiches,
	      ("sándwich" if n_sandwiches == 1 else "sándwiches") + ",",  # Solo para estética del mensaje.
	      "por un monto de", amount)
	print("\n\nGracias por su compra ¡Vuelva pronto!")
	
	voices.total_voice(n_sandwiches, amount)
