class Tweet:
    
	mensaje = ''
	user = ''
	MAX_PALABRAS_EN_TWEET = 15
	ListaNegra = ["bigote","enano","gordo","pelado"]

	def __init__(self, mensaje, user):
		self.mensaje = mensaje
		self.user = user

	def contienePalabra(self, palabra):
		for palabra in self.ListaNegra:
			if (self.mensaje.find(palabra)):
				return True
		return False
	
	def	tweetDirigido(self):
		return self.mensaje.find('@') != -1

	#def aQuienSeDirige(self):
	#	return list(filter(lambda x: x[0] in '@', self.mensaje.split(' ')))