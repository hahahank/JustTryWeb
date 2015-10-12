import time
import json
import urllib
from util import jsonRW
import settings
from util import  log


from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
# {'status': u'stop', 'pics': [], 'bu': u'ebg_bu3',
#  'producttype': [u'server', u'rack', u'eother', u'nb', u'pother'],
#  'productname': u'sf', 'specs': [], 'productid': u'sdfsd' }

CONFIG_FILE_PATH = settings.PRODUCTLIST
productMLog = log.Log('productM').logger
class ProductManager:

    productList={} 

#	{
#	  "999" :
#	    {
#        	"id":"999",
#	        "name":"test999",
#        	"bu":"pc",
#	        "status":"ready",
#	        "type":["server","rack"],
#	        "pic":[],
#        	"doc":[]
#	    }
#	}

    def __init__(self):
	productMLog.info("Init Product  Manager  ==")
	self.readConfig()
	productMLog.info("Init Product  Manager Done  ==")

    def readConfig(self):
	productMLog.info("readConfig")
	result = jsonRW.readConfig(CONFIG_FILE_PATH)
        self.productList = result

    def writeConfig(self,newjson):
	productMLog.info( "Write Config")
	result = jsonRW.writeConfig(CONFIG_FILE_PATH,newjson)
	productMLog.debug("Write config result :"+str(result))

    def getProductList(self):
	return self.productList

    def getListByType(self,type):
	for prod in self.productList.values():
	    prodTypes = prod['type']
	    for t in prodTypes:
		pass

    def insertProduct(self,pid,productInfo):
	productMLog.debug("Insert product : "+pid)
	pInfoJson = {}
	picList = []
	docList = []
        if(self.productList.get(pid) == None): 	# if product not exist
# 	    print "[PRO] Inset New Product ",productInfo
	    pInfoJson["name"] = productInfo['productname']
            pInfoJson["id"]   = productInfo['productid']
 	    pInfoJson["status"] = productInfo['status']
	    pInfoJson["type"] = productInfo['producttype']
	    pInfoJson["bu"]   = productInfo['bu']

	    id =  pInfoJson["id"]
            pInfoJson["pic"]  = []
	    pInfoJson["doc"]  = []
	    pics = productInfo['pics']
            docs = productInfo['specs']
	   
            # Save Pictures
	    imageTypes = ['jpg','jepg','jpe','bmp','gif','png',]
            for pic in pics:
		picTmp = pic.name.split(".")
		if(picTmp[1] not in imageTypes):
#		    print "[PRO] Image type Error:",pic.name
		    return (False,"Image type Error")
		picPath = 'product/'+id+'/pic/' # It is under "/static/media/" path
		picName = 'pic_'+id+"_"+pic.name
                path = default_storage.save(picPath+picName, ContentFile(pic.read())) # save file under its path
#		print 'Save Pic : ',picPath+picName,"==="
		picList.append(picPath+picName)

            # Save Documents
            for doc in docs:
		docPath = 'product/'+id+"/doc/"
		docName = 'doc_'+id+"_"+doc.name
 #               print 'Save Document : ',doc,"==="
	        path = default_storage.save(docPath+docName, ContentFile(doc.read()))
#		print 'Save Document : ',docPath+docName,"==="
		docList.append(docPath+docName)
	    pInfoJson['pic'] = picList
	    pInfoJson['doc'] = docList
	    self.productList[pInfoJson["id"]]=pInfoJson
	    self.writeConfig(self.productList)
	    return True	
	else:					# product is exist			
	    productMLog.warning("Insert Product is exist :"+pid)
	    return (False,"Product ID exist")



    def updateProduct(self,pid,config):
	pass

    def deleteProduct(self,pid):
	productMLog.info("Delete Product :"+pid)
	if(self.productList.get(pid) != None):
	    self.productList.pop(pid)		# Delete from memory
	    self.writeConfig(self.productList)	# Delete from config file
	    return True	    
	else:
	    productMLog.error("Delete Product error: Product Not Found : " +pid)
	    return False

    def getProductList(self):
	#print "product Manager : Get List"
	return self.productList

    def getPodcuctByID(self,proID):
#	print "product Manager : Get By ID"
	return self.productList.get(proID)
    
    def insetProduct(self,productInfo):
	if(self.productList.get(productInfo.get('productid') )==None):
	    self.productList[productInfo['productid']]=productInfo
	    productMLog.info("Insert Product Success: "+productInfo.get('productid'))
	    return True
	productMLog.debug("Insert Product ID Exist: "+productInfo.get('productid'))
	return False
