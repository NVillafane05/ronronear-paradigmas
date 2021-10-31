from Tweet import *

class Ronronear:
	tweets = []
	tweetsDirigidos = []
	tweetsNoDirigidos = []
	#bots = []
	#policia = []
	
	def recibirTweet(self, user, tweet):
		self.tweets.append(user + ": " + tweet)
		#if tweet.tweetDirigido():
	#		self.tweetsDirigidos.append(tweet)
	#	else:
	#		self.tweetsNoDirigidos.append(tweet)

	#	Tweet.contienePalabra(self,tweet)

	#def addBot(self, bot):
		#self.bots.append(bot)

	def printTweets(self):
		if (self.tweets):
			for i in self.tweets:
				print (i)
		else:
			print ("No hay tweets")