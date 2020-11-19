#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Valentina Figueroa <valenfiguer14@gmail.com>
"""Paquete orientado al pedido del usuario, incluyendo el cálculo de las órdenes y los mensajes mostrados por pantalla.

Módulos:

- `orders`: Relacionado con los cálculos de las órdenes.
- `msg`: Relacionado con los mensajes mostrados al usuario.
- `voices`: Relacionado con los mensajes de voz reproducidos por consola.

Funciones:

- `y_or_comma`: Solo para estética en el mensaje al usuario al listarle la orden completa (tamaño más ingredientes).
"""


__all__ = ['msg', 'orders', 'voices']


def y_or_comma(key: int, dictionary: dict) -> str:
	"""Mejora la estética al listar la orden de un sándwich, incluyendo el tamaño y los ingredientes adicionales.
	
	:argument key: Clave del valor usado en la función que llama a ésta.
	:argument dictionary: Diccionario que guarda los elementos usados en la función que llama a ésta
	"""

	if max(list(dictionary)) >= 1:
		if key == max(list(dictionary)):
			return str(" y ")
		else:
			return str(", ")
	else:
		return ""
