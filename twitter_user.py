from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
ckey='PIT4p2luB0KDNpAiwOhZAw'
csecret='g3oPAJozjQNC71YII6y5MmVYgRihwQsDZE2haHSUk'
atoken='109203663-4UrFweJVCvsREXqphEKhrIGGsmxJeBUoByogCzXo'
asecret='AaCT8vpu5dkuYSDv7CsNE0IfKGkhUMdJxDeCXtZNNjSAw'

followList = [38808354,21493892,24423060,135522740,76586556,18155773,27361341,22375230,275255334,151631847,259387326,184951676,27281797,36767117,59330116,93251387,230168526,73185825,259168090,71582989,149629307,46720050,1250032508,109203663]
class listener(StreamListener):
	
	def on_data(self,data):
		try:

			#print data
			data = data.strip()
			info = json.loads(data)
			if 'user' in info and len(info['user']['screen_name'])>0 and info['user']['id'] in followList:
				name = info['user']['screen_name']
				text = info['text']
				test = info['user']['id']
				print name+'::'+text+'::'+str(test)
			saveFile = open('oklahoma.txt','a')
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
#twitterStream.filter(follow = ["109203663"])
twitterStream.filter(follow = followList)
