
import settings
from util import googleSpreadsheets
gID = "1NhAyWXm9Q3CHTEDRJqyQG644dqx4zt6rlv2BCa1uIx4" # DS Video config file
vdoPath = settings.MEDIA_URL
from util import  log
LOGGER = log.Log('dsManager').logger


class vdoManager():

    vdoList = {}
    def __init__(self):
	self.vdoList = {}
	self.initListFromGogle()
 
    def initListFromGogle(self):
	tmp = googleSpreadsheets.gExParser(gID)
	if( tmp!=False ):	
	    self.vdoList = tmp
	'''
	{
	u'ex2.mp4': 	{u'status': u' 1', u' owner': u' 3', u' group': u' 2'}, 
	u'ex1.mp4': 	{u'status': u' 1', u' owner': u' 1', u' group': u' 1'}, 
	u'ex3.mp4': 	{u'status': u' 1', u' owner': u' 1', u' group': u' 1'}, 
	u'IMG_0851.MOV':{u'status': u' 0', u' owner': u' 4', u' group': u' 2'}, 
	u'mov_bbb.mp4': {u'status': u' 1', u' owner': u' 3', u' group': u' 2'}, 
	u'bb2.mp4': 	{u'status': u' 1', u' owner': u' 1', u' group': u' 1'}, 
	u'mycar2.mp4': 	{u'status': u' 1', u' owner': u' 2', u' group': u' 3'}
	}
	'''
	print "MANAGER : >>>",self.vdoList,"<<<"

    def getListByName(self):
	result = {}
	for k,v in self.vdoList.items():
	    if( int(v.get('status')) != 0):
		result[k]=v
	    else:
		print "status =0",k,v
	return result

    def getVdoByName(self):
	pass




