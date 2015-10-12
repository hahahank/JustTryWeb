import time
import json
import urllib

class PttManager:
    data={}
    def __init__(self):
	print "init PTT  TEST"
	self.go()

    def go(self):
	link = "https://www.kimonolabs.com/api/580b4oee?apikey=yYfFz7909q9qnLObDJF7tNELWNwoy3JQ"
#	print "ptt Go"
	myList = []
	hotList = json.load(urllib.urlopen(link)).get("results").get("collection1")
        self.data = hotList
#	print "get Data :" ,self.data
#	    time.sleep(10)
#	pass	
    def get(self):
	return self.data
