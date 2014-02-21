from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
ckey='PIT4p2luB0KDNpAiwOhZAw'
csecret='g3oPAJozjQNC71YII6y5MmVYgRihwQsDZE2haHSUk'
atoken='109203663-4UrFweJVCvsREXqphEKhrIGGsmxJeBUoByogCzXo'
asecret='AaCT8vpu5dkuYSDv7CsNE0IfKGkhUMdJxDeCXtZNNjSAw'

class listener(StreamListener):
	
	def on_data(self,data):
		try:

			print data
			saveFile = open('sachin.csv','a')
			saveFile.write(data)
			saveFile.write('\n')
			saveFile.close()
			return True
		except BaseException, e:
			print 'failed ondata,',str(e)
			time.sleep(5)
	def on_error(self, status):
		print status

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth,listener())
twitterStream.filter(track = ["sachin"])
