import json
import time
import urllib
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

import  log
JLOGGER = log.Log('jsonRW').logger

def readConfig(configFilePath):
    JLOGGER.info("Read Config File: "+ str(configFilePath))
    try:
        configFile = open(configFilePath,'r').read()	# Open config file (r)
        dictConfigFile = json.loads(configFile.replace("\n","").replace(" ",""))	# load the config 
    except:
	JLOGGER.error("Read Config file fail!!")
	return False
    JLOGGER.debug("Read Config Result :"+ str(dictConfigFile))
    return dictConfigFile

def writeConfig(configFilePath,newjson):
    JLOGGER.info("Write Config File: "+configFilePath)
    JLOGGER.debug("NewJson = "+str(newjson))
    c=0
    configFile = open(configFilePath,'r').read()        # Open config file (r)
    oldConfig = json.loads(configFile.replace("\n","").replace(" ",""))    # load the config
    configFile = open(configFilePath,'r+')  # Open config file (rw)
    configFile.truncate()                                   # Clean up the file
    while(c < 10):
	try:        
  	    json.dump(newjson,configFile)			# Dump the data
            configFile.flush()
	    break
	except:
   	    JLOGGER.error("Dump Data Error")
	    c += 1
    if(c>=10):
	JLOGGER.error("Dump Json Fail , Old Data:"+str(oldConfig))
	return False
    else:
	JLOGGER.debug("Dump Json Success")
    return True

