#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Valentina Figueroa <valenfiguer14@gmail.com>
"""Contiene las funciones relacionadas con los mensajes de voz al usuario.

Funciones:

- `talk(message)`: reproduce el mensaje de voz al usuario.
- `welcome_voices()`: bienvenida a la tienda.
- `number_sandwich_voice(n_order)`: número del sándwich actual.
- `sizes_list_voice()`: encabezado para la selección del tamaño del sándwich.
- `ingredients_list_voice()`: encabezado para la selección de los ingredientes adicionales.
- `sub_total_voice(order)`: resumen de la orden.
- `total_voice(n_sandwiches, amount`): resumen del pedido completo.
- `selected_size_voice(size)`: tamaño seleccionado.
- `confirmation_voice()`: confirmación de selección.
- `wrong_answer_voice()`: notificación de respuesta inválida.
- `ingredients_canceled_voice(election)`: notificación de cancelación de ingrediente(s).
- `next_order_voice()`: pregunta para continuar con la siguiente orden.
- `canceled_order_voice(n_order)`: notificación de cancelación de la orden actual.

Cómo funciona este módulo
=========================
(

1.  Importa el módulo datetime, del paquete del mismo nombre.

2.  Importa la clase `pyttsx3`.
	
	Si la operación falla:
	a)  Levanta la excepción ModuleNotFoundError.
	
	b)  Notifica al usuario que la funcionalidad de mensajes de voz por consola no está disponible.

3.  Creará el objeto de la clase `pyttsx`.

	Si la operación falla:
	a)  Levantará la excepción NameError al intentar ejecutar la siguiente instrucción::
			engine = pyttsx3.init()
	
	b)  Cambiará el valor de `module` a False, indicando que el módulo `pyttsx3` no fue importado.
	
4.  Si la clase fue importada, configurará velocidad, volumen y voz del objeto que reproducirá los mensajes por
consola.

	En la definición de funciones:
	
	a)  Se define la función `talk(message)`, que reproducirá los mensajes.
	
	b)  El resto de las funciones llamarán a `talk(message)`.
"""


from datetime import datetime
try:
	import pyttsx3
except ModuleNotFoundError:
	print("\nADVERTENCIA:\nNo se encontró la clase pyttsx3,"
	      " por lo que la funcionalidad de voz de este programa"
	      " no está disponible.\n\n")


module = True  # Confirmación que la clase pyttsx3 fue importada.
try:
	engine = pyttsx3.init()  # Creación del objeto.
except NameError:
	module = False  # Confirmación que el módulo pyttsx3 NO fue importado.

# CONFIGURACIÓN DE LA VOZ.
if module:
	engine.setProperty('rate', 145)  # Velocidad de la voz.
	engine.setProperty('volume', 1.0)  # Volumen de la voz.
	voices = engine.getProperty('voices')  # Obteniendo voz actual.
	# Cambiando voz a Español - HELENA (nombre de la voz según configuración de Microsoft).
	engine.setProperty('voice', 'spanish')


def talk(message: str):
	"""Ejecuta el mensaje de voz al usuario, por consola.
	
	Si no encuentra el módulo 'pyttsx3', la función no realizará nada.
	
	Argumentos:
	:argument message: Mensaje a reproducir por consola.
	"""
	
	if module:
		engine.say(message)
		engine.runAndWait()
		engine.stop()


def welcome_voice():
	"""Genera y pide reproducir el mensaje de bienvenida."""
	
	# Cambio de saludo según etapa del día. Solo por fines estéticos.
	if 5 <= datetime.now().hour < 12:
		message = "Buenos días..."
	elif 12 <= datetime.now().hour < 20:
		message = "Buenas tardes..."
	else:
		message = "Buenas noches..."
	message += """¡Bienvenido a SÁNDWICHES UCAB!
Realice su pedido a continuación..."""
	talk(message)


def number_sandwich_voice(n_order: str):
	"""Pide reproducir el número del sándwich perteneciente a la orden actual.
	
	Argumentos:
	:argument n_order: Número del sándwich.
	"""
	
	message = "Sándwich número" + n_order
	talk(message)


def sizes_list_voice():
	"""Pide reproducir el encabezado de la sección de selección de tamaño del sándwich."""
	
	message = "Por favor, elija el tamaño del sándwich a ordenar."
	talk(message)


def ingredients_list_voice():
	"""Pide reproducir el encabezado de la sección de selección de ingredientes adicionales."""
	
	message = "¿Desea algún ingrediente extra?"
	talk(message)


def sub_total_voice(order: str):
	"""Genera y pide reproducir el resumen de la orden actual.
	
	Argumentos:
	:argument order: Contiene la orden completa actual, con el tamaño e ingredientes adicionales seleccionados.
	"""
	
	message = "Usted seleccionó un sándwich " + order
	talk(message)


def total_voice(n_sandwiches: int, amount: int):
	"""Genera y pide reproducir el mensaje final del usuario antes de finalizar el programa.
	
	Contiene el encabezado del resumen del pedido; la cantidad total sándwiches pedidos junto con el monto total
	a pagar; y el mensaje de despedida del programa.
	
	Argumentos:
	:argument n_sandwiches: Número de sándwiches pedidos por el usuario.
	:argument amount: Monto total a pagar por el pedido.
	"""
	
	message = "Resumen del pedido"
	talk(message)
	message = "El pedido tiene un total de "\
	          + ("un sándwich" if n_sandwiches == 1 else str(n_sandwiches) + " sándwiches")\
	          + ", por un monto de " + str(amount)
	talk(message)
	message = "Gracias por su compra. ¡Vuelva pronto!"
	talk(message)


def selected_size_voice(size: str):
	"""Pide reproducir el tamaño del sándwich deseado por el usuario en el paso anterior."""
	
	message = "Tamaño solicitado: " + size
	talk(message)


def confirmation_voice():
	"""Pide reproducir el mensaje para confirmar de la opción seleccionada en el paso anterior."""
	
	message = "Por favor, confirme su elección."
	talk(message)


def wrong_answer_voice():
	"""Pide reproducir una notificación de respuesta inválida."""
	
	message = "¡¡Por favor, ingrese una respuesta válida!!"
	talk(message)


def canceled_ingredients_voice(election: str):
	"""Escoge y pide reproducir notificación de cancelación de ingredientes adicionales previamente seleccionados.
	
	Escoge mensaje a reproducir de acuerdo a la elección del usuario, en el paso anterior. Posteriormente, el mensaje
	escogido es enviado a ser reproducido.
	
	Argumentos:
	:argument election: Elección del usuario, en el paso anterior, siendo 'reg' o 'can'.
	"""
	
	if election == 'reg':
		message = "ATENCIÓN: último ingrediente eliminado de la orden."
	else:
		message = "ATENCIÓN: todos los ingredientes eliminados de la orden"
	talk(message)


def next_order_voice():
	"""Pide reproducir pregunta sobre realización de la siguiente orden."""
	message = "¿Desea continuar?"
	talk(message)


def canceled_order_voice(n_order: str):
	"""Pide reproducir la notificación de cancelación de la orden actual."""
	
	message = "ATENCIÓN: ¡¡Orden" + n_order + "cancelada!!"
	talk(message)


def interruption_goodbye_voice(message: str):
	talk(message)
