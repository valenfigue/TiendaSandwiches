#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == "__main__":
	from DB import sizes
	from DB import ingredients as ing
	from Messages import orders, msg
	
	# Ingredientes para hacer los sándwiches
	dict_sizes = sizes.get_sizes()
	dict_ing = ing.get_ingredients()
	
	# Directorio que guarda toda la información de las órdenes
	order = {1: {"size": dict(),  # Visualización del directorio
	             "ing": {1: dict()}}}
	n_order = max(list(order))  # Número de orden del usuario
	
	total = 0  # Total a pagar
	sub_total = 0  # Sub total a pagar
	# Confirmación para realizar la siguiente orden de sándwich
	next_order = 's'
	
	msg.welcome()  # Mensaje de bienvenida
	
	if dict_sizes:
		if not dict_ing:
			msg.error_ingredients()
		
		while next_order == 's':  # Mientras que se quiera otra orden...
			print("\n\nSándwich número", n_order)
			
			order.update({n_order: {"size": orders.size_order(dict_sizes)}})
			
			# Solo si encontró el archivo "additionalingredients.txt"
			if dict_ing:
				order[n_order].update({"ing": orders.ingredients_order(dict_ing)})
			
			next_order, sub_total = orders.subtotal(order.get(n_order))
			total += sub_total
			
			if next_order == 'n':  # Ya no se desean más órdenes..
				orders.total(n_order, total)
			elif next_order == 'can':  # Cancelar la orden actual.
				print("ATENCIÓN: ¡¡Orden", n_order, "cancelada!!")
				next_order = 's'
				order.pop(n_order)
			else:  # Realizar otra orden
				n_order += 1
	else:
		msg.error_sizes()
