# -*- coding: utf-8 -*-
import os.path
import rrdtool
import settings

RRA_5m  = "1"
RRA_30m = "6"
RRA_1h = "12"
RRA_2h = "24"
RRA_6h = "72"
RRA_12h = "144"
RRA_1d =  "288"
RRA_2d =  "576"
RRA_7d = "2016"

class RrdModel:
    """ RRDtool interface"""

    def __init__(self,name="test.rrd",step=300,vertical_label="Y"):
	self.id = name.replace(".rrd","")
	self.step = step 	# interval
	self.vertical_label= vertical_label  	# Y label
	self.name = os.path.join(settings.RRDPATH,name) # rrd file path & name
#	print self.__str__()
	if not self.__checkDbExist() :
	    self.create()
    
    def __str__(self):
	print "[RRD] Infomation:"
	print "\tName > ",self.name
	print "\tStep > ",self.step,"\t,Y-label > ",self.vertical_label

    def __checkDbExist(self):
	if (os.path.isfile(self.name) ):
	    return True
	return False

    def create(self):
	''' Create & Setting the rrd file'''
#	print "[RRD] Create RRD File: ", self.name
	interval = str(self.step) 
        interval_mins = float(interval) / 60  
        heartbeat = str(int(interval) * 2)
        ds_string = [ 'DS:{0}:GAUGE:{1}:U:U'.format(self.id, heartbeat),] # 1. COUNTER => 相對值 , GAUGE => 絕對值 2. :U => 無限制

        rrdtool.create( 
	    str(self.name),
	    #'--start', '920804400',
	    "--step", interval, 
            ds_string,
            'RRA:AVERAGE:0.5:{0}:{1}'.format(RRA_5m ,"500" ), # 在'1'個step內 最多紀錄'500'次 資料平均值
            'RRA:AVERAGE:0.5:{0}:{1}'.format(RRA_30m ,'500' ), # 6 * 5 = 30 min
	    'RRA:AVERAGE:0.5:{0}:{1}'.format(RRA_2h,'500' ), # 24 * 5 = 120 min = 2h
	    "RRA:AVERAGE:0.5:{0}:{1}".format(RRA_2d,"500" ) # 576 * 5 = 2 Day
	)

    def update(self):
	print "[RRD] Update RRD Date: ", self.name

    def fatch(self,start_time="-1d",rra=RRA_30m):
	r =  int(rra)*int(self.step)
#	print int(rra),int(self.step),r
#	print "Fatch Command",str(self.name),"AVERAGE","-s",str(start_time),"-r",str(r)
	result = rrdtool.fetch(str(self.name),"AVERAGE","-s",str(start_time),"-r",str(r) )
	result_start = result[0][0]
	result_end = result[0][1]
	result_step = result[0][2]
	ds_name = result[1]
#	print "Get Result :",	 result 
	return result


    def graph(self):
	print "[RRD] Get RRD Greph: ", self.name       

