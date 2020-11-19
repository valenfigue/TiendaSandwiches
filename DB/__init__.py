#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contiene los módulos que trabajan sobre los archivos .txt con la información de los ingredientes para los sándwiches.

Módulos:
- `ingredients`: Relacionado con los ingredientes adicionales.
- `sizes`: Relacionado con los tamaños de los sándwiches.
- `reading_files`: Relacionados con la lectura y escritura de archivos de texto.

Constantes:
- `FOLDER`: Ruta raíz de todos los archivos de texto usados en este programa.
"""


from pathlib import Path


__all__ = ['ingredients', 'sizes', 'files', 'FOLDER']

FOLDER = Path("DB/files/")  # Ruta que contiene a todos los archivos de texto.
