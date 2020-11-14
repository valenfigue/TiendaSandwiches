#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == "__main__":
	from DB import sizes
	from DB import ingredients as ing
	from Messages import orders, msg
	
	# Ingredientes para hacer los sándwiches
	dict_sizes = sizes.get_sizes()
	dict_ing = ing.get_ingredients()
	
	# Información de las órdenes
	order = {1: {"size": dict(),
	             "ing": {1: dict()}}}
	n_order = max(list(order))  # Número de orden del usuario
	
	total = 0  # Total a pagar
	sub_total = 0  # Sub total a pagar
	# Confirmación para realizar la siguiente orden de sándwich
	next_order = 's'
	
	msg.hello()  # Mensaje de bienvenida
	
	if dict_sizes:
		if not dict_ing:
			msg.error_ingredients()
		
		while next_order == 's':
			print("Sándwich número", n_order)
			
			order[n_order]["size"] = orders.size_order(dict_sizes)
			
			# Solo si encontró el archivo "additionalingredients.txt"
			if dict_ing:
				order[n_order]["ing"] = orders.ingredients_order(dict_ing)
			
			next_order, sub_total = orders.subtotal(order[n_order])
			total += sub_total
			
			if next_order == 'n':
				orders.total(n_order, total)
			else:
				n_order += 1
				order[n_order] = {"size": dict(),
				                  "ing": {1: dict()}}
	else:
		msg.error_sizes()
