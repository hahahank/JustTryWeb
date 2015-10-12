COMMAND={"sensor":"sdr","network":"lan print","machine":"mc info","power":"power status"}


class MachineManager():
    machineList = {}
    def __init__(self,):
	pass
    
    def getApiFormatSensor(self,data):
	result =[]
	for sdrInfo  in data:
	    if(len(sdrInfo["value"]) == 2):
	        result.append([sdrInfo["item"],sdrInfo["value"][0],sdrInfo["value"][1],sdrInfo["status"]]) # [item ,value ,unit ,status]
	    else:
		result.append([sdrInfo["item"],sdrInfo["value"][0],"",sdrInfo["status"]]) # [item ,value ,unit ,status]
	print "MManager Get sensor",result
	return result

    def getApiFormatNetwork(self,data):
        result =[]
        for netInfo  in data:
            result.append([netInfo["item"],netInfo["value"]] ) # [item ,value ,unit ,status]
        return result

    def getApiFormatMachine(self,data):
        result =[]
        for mcInfo  in data:
            result.append([ mcInfo["item"],mcInfo["value"] ]) # [item ,value ,unit ,status]
        return result

    def getApiFormatPower(self,data):
	result = []
	for power in data:
	    result.append([ power["power"] ])
	return result 

    def getMachineInfo(self,bmc,ipmi):
	machineInfos = self.machineList.get(bmc)
	if(machineInfos == None): return False
	if(ipmi == "sensor"): return self.getApiFormatSensor(machineInfos[ipmi])
	elif(ipmi == "network"): return self.getApiFormatNetwork(machineInfos[ipmi])
	elif(ipmi == "machine"): return self.getApiFormatMachine(machineInfos[ipmi])
	elif(ipmi == "power") : return self.getApiFormatPower(machineInfos[ipmi])


    def getAllInfo(self):
	return self.machineList
    
    def updateIpmi(self,data):
#	print "MManager update ipmi ", data
#	print "BMC : ",data.get("BMC")[0],""
	if data.get("BMC")[0] == None:	# Check BMC IP IN DATA
	    return False 	
	bmc_ip = data.get("BMC")[0]
	if bmc_ip  not in self.machineList: # Init the Item in the List
	    self.machineList[bmc_ip] = {}
	for k in COMMAND.keys():	# Check IPMI DATA KEYS
	    if k not in data:
		print "Key error",k
		return False	
	for k , v in data.items():	# Update Data
	    if(k!="BMC"):
		self.machineList[bmc_ip][k] = v
	print self.machineList
	return True
