#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
try:
	import pyttsx3
except ModuleNotFoundError:
	print("\nADVERTENCIA:\nNo se encontró el módulo pyttsx3,"
	      " por lo que la funcionalidad de voz de este programa"
	      " no está disponible.\n\n")


module = True
# Configuración de la voz.
try:
	engine = pyttsx3.init()  # Creación del objeto.
except NameError:
	module = False
	
if module:
	engine.setProperty('rate', 145)  # Velocidad de la voz.
	engine.setProperty('volume', 1.0)  # Volumen de la voz.
	voices = engine.getProperty('voices')  # Obteniendo voz actual.
	# Cambiando voz a Español - HELENA (nombre de la voz según configuración de Microsoft).
	engine.setProperty('voice', 'spanish')


def talk(message: str):
	if module:
		engine.say(message)
		engine.runAndWait()
		engine.stop()


def welcome_voice():
	# Cambio de saludo según etapa del día.
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
	message = "Sándwich número" + n_order
	talk(message)


def sizes_list_voice():
	message = "Por favor, elija el tamaño del sándwich a ordenar."
	talk(message)


def ingredients_list_voice():
	message = "¿Desea algún ingrediente extra?"
	talk(message)


def sub_total_voice(order: str):
	message = "Usted seleccionó un sándwich " + order
	talk(message)


def total_voice(n_sandwiches: int, amount: int):
	message = "Resumen del pedido"
	talk(message)
	message = "El pedido tiene un total de "\
	          + ("un sándwich" if n_sandwiches == 1 else str(n_sandwiches) + " sándwiches")\
	          + ", por un monto de " + str(amount)
	talk(message)
	message = "Gracias por su compra. ¡Vuelva pronto!"
	talk(message)


def selected_size_voice(size: str):
	message = "Tamaño solicitado: " + size
	talk(message)


def confirmation_voice():
	message = "Por favor, confirme su elección."
	talk(message)


def wrong_answer_voice():
	message = "¡¡Por favor, ingrese una respuesta válida!!"
	talk(message)


def ingredients_canceled_voice(election: str):
	if election == 'reg':
		message = "ATENCIÓN: último ingrediente eliminado de la orden."
	else:
		message = "ATENCIÓN: todos los ingredientes eliminados de la orden"
	talk(message)


def next_order_voice():
	message = "¿Desea continuar?"
	talk(message)


