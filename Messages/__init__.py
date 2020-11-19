#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Paquete orientado al pedido del usuario, incluyendo el cálculo de las órdenes y los mensajes mostrados por pantalla.

Módulos:
orders -- Relacionado con los cálculos de las órdenes.
msg -- Relacionado con los mensajes mostrados al usuario.
"""


__all__ = ['msg', 'orders', 'voices']


def y_or_comma(key: int, dictionary: dict):
	"""Solo para estética en el mensaje al usuario.
	
	:argument key Clave del valor usado en la función que llama a ésta.
	:argument dictionary Diccionario que guarda los elementos usados en la función que llama a ésta
	"""

	if max(list(dictionary)) >= 1:
		if key == max(list(dictionary)):
			return str(" y ")
		else:
			return str(", ")
	else:
		return ""
