import urllib2
import json
import  log
LOGGER = log.Log('googleDB').logger

def gExParser(gID):
    url="https://spreadsheets.google.com/feeds/list/"+gID+"/1/public/basic?alt=json"
    req = urllib2.Request(url)
    result = {}
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    data = json.loads(res)
    for k in data.get('feed').get('entry'):
        r = {}
        for i in k.get(u'content').get(u'$t').split(','):
            rk = i.split(':')[0]
            rv = i.split(':')[1]
            r[rk] = rv
        #print r,"<<<" 
        result[k.get('title').get('$t')] = r
#        print ">>>> ",k.get('title').get('$t')," : ",r
        #print ""
    LOGGER.debug("Get Google DB:",result);
    return result

    
if __name__ == '__main__':
    gID = "1NhAyWXm9Q3CHTEDRJqyQG644dqx4zt6rlv2BCa1uIx4" # DS
#    gID2 ="1QY-QUaQkEnbWQ0dkz0jFB7HS4HJN3Ji1NqMBOsBqseU"
    print gExParser(gID)
    
