def get_dictionary(file):
	"""Lee el contenido de un archivo y genera un diccionario
	con la información del alimento (nombre y precio)"""
	
	dictionary = dict()  # Donde se guardarán el contenido.
	
	f = open(file, 'r', encoding='utf-8')
	f.readline()
	f.readline()
	while True:  # Lectura de archivo
		key_ = f.readline()[0:-1]  # Obteniendo la clave
		
		if not key_:  # Si no hay más líneas, rompe el ciclo.
			break
		
		# Obteniendo el nombre
		name_ = f.readline()[0:-1]
		# Obteniendo su precio
		price = float(f.readline()[0:-1])
		# Guardando to.do lo anterior, en un diccionario
		dictionary.update({key_: [name_, price]})
	f.close()

	return dictionary
