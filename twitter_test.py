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
			dirty = open('syria_full.txt','a')
			encode = data.encode('ascii','ignore')
			dirty.write(encode)
			dirty.write('\n')
			dirty.close()
			tweet = data.split(',"text":"')[1].split('","source')[0]
			print tweet
			#saveThis = str(time.time())+'::'+tweet
			saveFile = open('syria_clean.txt','a')
			saveFile.write(tweet)
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
twitterStream.filter(track = ["syria"])

