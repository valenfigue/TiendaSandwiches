#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Valentina Figueroa <valenfigue14@gmail.com>
# Date: 2020-11-19
"""Programa en Python sobre el mini proyecto 'Tienda de Sándwiches UCAB', de la electiva 'Programando con Python', UCAB.

Funciones:

- `tienda()`: función principal del programa.

Cómo funciona este módulo
=========================
1.  Importa los paquetes DB, junto con sus módulos, y Messages, junto con los módulos orders y msg.
	
2.  Define una función que simula el flujo de una tienda de sándwiches. Puede levantar la excepción KeyboardInterrupt
por combinación de teclas de interrupción dentro de la consola.
	
	Dentro de la definición de la función:
	
	a)  Se define los diccionarios con los ingredientes para los sándwiches::
		dict_sizes
		dict_ing
		
	b)  Se define el diccionario que contendrá cada orden del usuario::
		order = {número de la orden: {"size": info del tamaño, "ing": info de los ingredientes,
		"subtotal": monto por esa orden}}
	
	d)  Se maneja el caso de no encontrar los archivos que contienen los ingredientes y tamaños.
"""
__docformat__ = 'restructuredtext'

from DB import sizes, ingredients as ing
from Messages import orders, msg


def tienda():
	"""Función principal del programa.
	
	Saluda al usuario y toma su orden, que incluye el tamaño del sándwich y los ingredientes adicionales que desea.
	Muestra e indica, por voz, el resumen de la orden y le pregunta si quiere realizar otra orden. Si es afirmativo,
	se reinicia el ciclo. Cuando ya no sea afirmativo, muestra e indica, por voz, el resumen del pedido.
	
	:exception KeyboardInterrupt: si, por consola, el programa se interrumpe por combinación de teclas de interrupción.
	"""
	
	# Ingredientes para hacer los sándwiches.
	dict_sizes = sizes.get_sizes()  # Tamaños.
	dict_ing = ing.get_ingredients()  # Ingredientes adicionales.
	
	# Visualización del directorio que guarda toda la información de cada orden del pedido.
	# Contiene:
	order = {1: {  # Número de la orden. Para cada orden:
		"size": {  # El tamaño del sándwich.
			"name": str(),  # Nombre del tamaño.
			"price": 0},  # Precio.
		"ing": {1: {  # Los ingredientes adicionales. Para cada ingrediente.
			"name": str(),  # Nombre del ingrediente.
			"price": 0}},  # Precio.
		"sub_total": 0}}  # El sub total de la orden.
	
	n_order = 1  # Número de orden del usuario.
	next_order = 's'  # Confirmación para realizar la siguiente orden de sándwich
	
	# INICIO
	if dict_sizes:
		if not dict_ing:  # En caso de que no encuentre el archivo "additionalingredients.txt" o este esté vacío.
			msg.error_ingredients()
		msg.welcome()  # Mensaje de bienvenida.
		try:
			while next_order == 's':  # Mientras que se quiera otra orden...
				msg.number_sandwich(n_order)
				
				# REALIZACIÓN DE LA ORDEN.
				# Pregunta sobre el tamaño de sándwich.
				order.update({n_order: {"size": orders.size_order(dict_sizes)}})
				
				# Pregunta sobre los ingredientes adicionales.
				if dict_ing:  # Solo si encontró el archivo "additionalingredients.txt"
					order[n_order].update({"ing": orders.ingredients_order(dict_ing)})
				else:  # En caso de que no encuentre el archivo
					# "additionalingredients.txt" o este esté vacío.
					order[n_order].update({"ing": {}})
				
				# CÁLCULOS DE LA ORDEN.
				# Cálculo del subtotal de la orden y confirmación de siguiente orden.
				next_order = orders.subtotal(order.get(n_order))
				
				# Cálculo del total del pedido.
				if next_order == 'n':  # Ya no se desea realizar más órdenes...
					orders.total(order)  # Resumen del pedido.
				
				elif next_order == 'can':  # Cancelar la orden actual
					next_order = orders.canceled_order(n_order, order)  # Cancelación de la orden.
				
				else:  # Sí se desea tomar otra orden...
					n_order += 1
			else:
				msg.ending()  # Salida del programa.
		except KeyboardInterrupt:  # En caso de interrumpir el programa por consola con combinación de teclas CONTROL+C.
			msg.interruption_goodbye()
			
	else:  # En caso de que no encuentre el archivo "sandwichsizes.txt" o este esté vacío.
		msg.error_sizes()


if __name__ == "__main__":
	tienda()
