import os.path
import rrdtool
import settings
import rrdModel

class RrdManager:
    """ RRDtool interface"""

    def __init__(self):
    #  RRDLIST = [{'name':'test.rrd','step':300,'vertical_label':'Y'}, ]  
	self.rrdList={}
 	for r in settings.RRDLIST:
  	    self.rrdList[r['name']] = rrdModel.RrdModel( r['name'],r['step'],r['vertical_label'] )

    def getData(self,file_name='test.rrd',start_time="-2d",rra="1800"):
	return self.rrdList.get(file_name).fatch()
