from Tweet import *
from Ronronear import *
class Main():
	ronronear = Ronronear()

	usuario = "@"+input("Ingrese su usuario: ")
	print("Bienvenido/a "+usuario+"\n")
	
	while (True):
		try:
			op = int(input("1. Add tweet\n2. Cambiar de usuario\n3. Ver usuarios - tweets\n4. Salir\n"))
		
			if(op==4): 
				break
			else:
				if (op==2):
					usuario = "@"+input("Ingrese su usuario: ")
					print("Bienvenido/a "+usuario+"\n")
				elif (op==1):
					myTweet = input("Add tweet: ")
					if (len(myTweet.split(' '))>15):
						print ("Por favor, el tweet debe tener solo 15 palabras")
					else:
						ronronear.recibirTweet(usuario,myTweet)
				elif (op==3):
					 ronronear.printTweets()

		except ValueError:
			print ("Por favor, ingrese una opción correcta")

	print ("¡Hasta la próxima!")

	#	tweet = Tweet('HOLA  @sspalisa', 'sspalisa')

	#	print(tweet.mensaje)
	#	print(tweet.user)
	#	print(tweet.longitudInvalida())
	#	print(tweet.tweetDirigido())
	#	print(tweet.aQuienSeDirige())
