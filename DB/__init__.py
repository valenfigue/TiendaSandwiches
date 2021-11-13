#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contiene los módulos que trabajan sobre los archivos .txt con la información de los ingredientes para los sándwiches.

Módulos:
- `ingredients`: Relacionado con los ingredientes adicionales.
- `sizes`: Relacionado con los tamaños de los sándwiches.
- `reading_files`: Relacionados con la lectura y escritura de archivos de texto.

Funciones:
- `resolver_ruta()`: Resuelve la ruta de los archivos de texto.

Constantes:
- `FOLDER`: Ruta raíz de todos los archivos de texto usados en este programa.
"""


from pathlib import Path
import os
import sys


__all__ = ['ingredients', 'sizes', 'files', 'FOLDER', 'resolver_ruta']

FOLDER = Path("DB/files/")  # Ruta que contiene a todos los archivos de texto.


def resolver_ruta(ruta_relativa: str):
	"""Resuelve las rutas dependiendo del entorno, es decir, si está empaquetado o no.
	
	Si el programa no está empaquetado, buscará la ruta normal. Si el archivo ya está empaquetado, la función
	resolverá la ruta en donde se empaquetan los assets.
	
	@author parzibyte
	
	:param ruta_relativa: Ruta del archivo a resolver por la función.
	"""
	
	if hasattr(sys, '_MEIPASS'):
		return os.path.join(sys._MEIPASS, ruta_relativa)
	return os.path.join(os.path.abspath('.'), ruta_relativa)
