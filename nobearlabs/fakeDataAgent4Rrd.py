import rrdtool
import time
import random 
import threadpool

def updateRRD(d):
    rSec = int(random.random()*100)
    time.sleep( d )
    now = time.time()
    rrdtool.update('/home/ubuntu/mySite/rrd/db/test.rrd',"{0}:{1}".format(now,rSec) )
    print "[RRD] update now : ",now,"  ,data : ",rSec , "d ",d



counter = 0
pool = threadpool.ThreadPool()
while(True):
    delays = [random.randrange(1, 100) for i in range(100)]
    for i, d in enumerate(delays):
        pool.add_task(updateRRD,d)
    time.sleep( 30 ) # 1 ~ 99 sec
    counter+=1
    if (counter > 300):
        break

pool.wait_completion()
