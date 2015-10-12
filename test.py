import os,json
import platform
import urllib2, urllib

osType = platform.system()
windows_os = "Windows"
linux_os = "Linux"
trueData = True


ipmiSettings = {
         windows_os :"D:\\tools\ipmitool\\ipmitool.exe",
         linux_os:"ipmitool",
         "IP":["10.3.211.114","10.3.211.130"],
         "USER":"admin",
         "PASSWORD":"admin",
         "COMMAND":{"sensor":"sdr","network":"lan print","machine":"mc info","power":"power status"}
         
        } 
ipmitool = ipmiSettings[osType]

def exeIpmiCommand(command,ip):
    if(trueData == False):
        print command
        if(command == "lan print"):
            data =  """Set in Progress         : Set Complete
Auth Type Support       : NONE MD2 MD5 PASSWORD
Auth Type Enable        : Callback : NONE MD2 MD5 PASSWORD
                        : User     : NONE MD2 MD5 PASSWORD
                        : Operator : NONE MD2 MD5 PASSWORD
                        : Admin    : NONE MD2 MD5 PASSWORD
                        : OEM      :
IP Address Source       : DHCP Address
IP Address              : 0.0.0.0
Subnet Mask             : 0.0.0.0
MAC Address             : 00:8c:fa:56:fb:4a
SNMP Community String   : AMI
IP Header               : TTL=0x40 Flags=0x40 Precedence=0x00 TOS=0x10
BMC ARP Control         : ARP Responses Enabled, Gratuitous ARP Disabled
Gratituous ARP Intrvl   : 0.0 seconds
Default Gateway IP      : 0.0.0.0
Default Gateway MAC     : 00:00:00:00:00:00
Backup Gateway IP       : 0.0.0.0
Backup Gateway MAC      : 00:00:00:00:00:00
802.1q VLAN ID          : Disabled
802.1q VLAN Priority    : 0
RMCP+ Cipher Suites     : 0,1,2,3,6,7,8,11,12
Cipher Suite Priv Max   : caaaXXaaaXXaaXX
                        :     X=Cipher Suite Unused
                        :     c=CALLBACK
                        :     u=USER
                        :     o=OPERATOR
                        :     a=ADMIN
                        :     O=OEM"""
        
        if(command == "sdr"):
            data = """ MLB TEMP 1       | 28 degrees C      | ok
MLB TEMP 2       | 33 degrees C      | ok
MLB TEMP 3       | 30 degrees C      | ok
MLB TEMP 4       | 30 degrees C      | ok
MLB TEMP 5       | 30 degrees C      | ok
MLB TEMP 6       | 30 degrees C      | ok
MLB TEMP 7       | 29 degrees C      | ok
MLB TEMP 8       | 27 degrees C      | ok
MLB TEMP 9       | 29 degrees C      | ok
MLB TEMP 10      | 27 degrees C      | ok
MB Ambient       | 26 degrees C      | ok
CPU 1 Temp       | 35 degrees C      | ok
CPU 2 Temp       | 39 degrees C      | ok
CPU1 PECI ABS    | 53 degrees C      | ok
CPU2 PECI ABS    | 49 degrees C      | ok
CPU1 Status      | 0 unspecified     | ok
CPU2 Status      | 0 unspecified     | ok
VCORE1           | 0.81 Volts        | ok
VCORE2           | 0.81 Volts        | ok
STBY 5V          | 4.80 Volts        | ok
PS 5V            | 5.05 Volts        | ok
PS 12.XV         | 12.16 Volts       | ok
PS 3.3V          | 3.29 Volts        | ok
PS 1.1V          | 1.10 Volts        | ok
INLET FAN 1      | 0 RPM             | nr
INLET FAN 2      | 0 RPM             | nr
INLET FAN 3      | 3840 RPM          | ok
INLET FAN 4      | 0 RPM             | nr
INLET FAN 5      | 3840 RPM          | ok
INLET FAN 6      | 0 RPM             | nr
INLET FAN 7      | 3920 RPM          | ok
PSU1 Status      | Not Readable      | ns
PSU2 Status      | Not Readable      | ns
PSU Power In     | 0 Watts           | ok
PSU Redundancy   | Not Readable      | ns
ACPI Pwr State   | 0x00              | ok
SEL Fullness     | 0 unspecified     | ok
PEF Action       | 0 unspecified     | ok
Watchdog2        | 0 unspecified     | ok
Memory           | 0 unspecified     | ok
PCI BUS          | 0 unspecified     | ok"""
        if(command == "mc info"):
            data = """Device ID                 : 36
Device Revision           : 1
Firmware Revision         : 2.23
IPMI Version              : 2.0
Manufacturer ID           : 6569
Manufacturer Name         : Unknown (0x19A9)
Product ID                : 54 (0x0036)
Product Name              : Unknown (0x36)
Device Available          : yes
Provides Device SDRs      : no
Additional Device Support :
    Sensor Device
    SDR Repository Device
    SEL Device
    FRU Inventory Device
    IPMB Event Receiver
    IPMB Event Generator
    Chassis Device
Aux Firmware Rev Info     :
    0x00
    0x00
    0x00
    0x00"""


    else:
    
    
        cmd = ipmitool + " -U "+ipmiSettings.get("USER")+" -P "+ipmiSettings.get("PASSWORD")
        cmd = cmd + " -H " + ip +" "+ command
        #print ">>",cmd,"<<"
        result = os.popen(cmd)
        data = result.read()
        #print ">>",data,"<<"
    print data
    return data
    
    
def sdrParser(data):
    '''[
    {'status': 'ok', 'item': 'MLB TEMP 1', 'value': ['28', 'degrees C']}, 
    {'status': 'ok', 'item': 'MLB TEMP 2', 'value': ['33', 'degrees C']}, 
    {'status': 'ok', 'item': 'MLB TEMP 3', 'value': ['30', 'degrees C']}, 
    {'status': 'ok', 'item': 'MLB TEMP 4', 'value': ['30', 'degrees C']}, {'status': 'ok', 'item': 'MLB TEMP 5', 'value': [['30', 'degrees C']]}, {'status': 'ok', 'item': 'MLB TEMP 6', 'value': [['30', 'degrees C']]}, {'status': 'ok', 'item': 'MLB TEMP 7', 'value': [['29', 'degrees C']]}, {'status': 'ok', 'item': 'MLB TEMP 8', 'value': [['27', 'degrees C']]}, {'status': 'ok', 'item': 'MLB TEMP 9', 'value': [['29', 'degrees C']]}, {'status': 'ok', 'item': 'MLB TEMP 10', 'value': [['27', 'degrees C']]}, {'status': 'ok', 'item': 'MB Ambient', 'value': [['26', 'degrees C']]}, {'status': 'ok', 'item': 'CPU 1 Temp', 'value': [['35', 'degrees C']]}, {'status': 'ok', 'item': 'CPU 2 Temp', 'value': [['39', 'degrees C']]}, {'status': 'ok', 'item': 'CPU1 PECI ABS', 'value': [['53', 'degrees C']]}, {'status': 'ok', 'item': 'CPU2 PECI ABS', 'value': [['49', 'degrees C']]}, {'status': 'ok', 'item': 'CPU1 Status', 'value': [['0', 'unspecified']]}, {'status': 'ok', 'item': 'CPU2 Status', 'value': [['0', 'unspecified']]}, {'status': 'ok', 'item': 'VCORE1', 'value': [['0.81', 'Volts']]}, {'status': 'ok', 'item': 'VCORE2', 'value': [['0.81', 'Volts']]}, {'status': 'ok', 'item': 'STBY 5V', 'value': [['4.80', 'Volts']]}, {'status': 'ok', 'item': 'PS 5V', 'value': [['5.05', 'Volts']]}, {'status': 'ok', 'item': 'PS 12.XV', 'value': [['12.16', 'Volts']]}, {'status': 'ok', 'item': 'PS 3.3V', 'value': [['3.29', 'Volts']]}, {'status': 'ok', 'item': 'PS 1.1V', 'value': [['1.10', 'Volts']]}, {'status': 'nr', 'item': 'INLET FAN 1', 'value': [['0', 'RPM']]}, {'status': 'nr', 'item': 'INLET FAN 2', 'value': [['0', 'RPM']]}, {'status': 'ok', 'item': 'INLET FAN 3', 'value': [['3840', 'RPM']]}, {'status': 'nr', 'item': 'INLET FAN 4', 'value': [['0', 'RPM']]}, {'status': 'ok', 'item': 'INLET FAN 5', 'value': [['3840', 'RPM']]}, {'status': 'nr', 'item': 'INLET FAN 6', 'value': [['0', 'RPM']]}, {'status': 'ok', 'item': 'INLET FAN 7', 'value': [['3920', 'RPM']]}, {'status': 'ns', 'item': 'PSU1 Status', 'value': [['Not', 'Readable']]}, {'status': 'ns', 'item': 'PSU2 Status', 'value': [['Not', 'Readable']]}, {'status': 'ok', 'item': 'PSU Power In', 'value': [['0', 'Watts']]}, {'status': 'ns', 'item': 'PSU Redundancy', 'value': [['Not', 'Readable']]}, {'status': 'ok', 'item': 'ACPI Pwr State', 'value': [['0x00']]}, {'status': 'ok', 'item': 'SEL Fullness', 'value': [['0', 'unspecified']]}, {'status': 'ok', 'item': 'PEF Action', 'value': [['0', 'unspecified']]}, {'status': 'ok', 'item': 'Watchdog2', 'value': [['0', 'unspecified']]}, {'status': 'ok', 'item': 'Memory', 'value': [['0', 'unspecified']]}, {'status': 'ok', 'item': 'PCI BUS', 'value': [['0', 'unspecified']]}
    ]
    '''
    dataItem=[]
    for d in data.splitlines() :
        tmp = []
        for i in  d.split("|"):
            tmp.append(" ".join(i.split())  )
        dataItem.append({  "item":tmp[0], "value":tmp[1].replace(" ","|",1).split("|"), "status":tmp[2]  })   
    return dataItem    

def lanParser(data):
    '''[
    {'status': None, 'item': 'Set in Progress', 'value': ['Set Complete']}, 
    {'status': None, 'item': 'Auth Type Support', 'value': ['NONE MD2 MD5 PASSWORD']}, 
    {'status': None, 'item': 'Auth Type Enable', 'value': ['Callback : NONE MD2 MD5 PASSWORD', 'User : NONE MD2 MD5 PASSWORD', 'Operator : NONE MD2 MD5 PASSWORD', 'Admin : NONE MD2 MD5 PASSWORD', 'OEM :']}, 
    {'status': None, 'item': 'IP Address Source', 'value': ['DHCP Address']}, 
    {'status': None, 'item': 'IP Address', 'value': ['0.0.0.0']}, {'status': None, 'item': 'Subnet Mask', 'value': ['0.0.0.0']}, {'status': None, 'item': 'MAC Address', 'value': ['00:8c:fa:56:fb:4a']}, {'status': None, 'item': 'SNMP Community String', 'value': ['AMI']}, {'status': None, 'item': 'IP Header', 'value': ['TTL=0x40 Flags=0x40 Precedence=0x00 TOS=0x10']}, {'status': None, 'item': 'BMC ARP Control', 'value': ['ARP Responses Enabled, Gratuitous ARP Disabled']}, {'status': None, 'item': 'Gratituous ARP Intrvl', 'value': ['0.0 seconds']}, {'status': None, 'item': 'Default Gateway IP', 'value': ['0.0.0.0']}, {'status': None, 'item': 'Default Gateway MAC', 'value': ['00:00:00:00:00:00']}, {'status': None, 'item': 'Backup Gateway IP', 'value': ['0.0.0.0']}, {'status': None, 'item': 'Backup Gateway MAC', 'value': ['00:00:00:00:00:00']}, {'status': None, 'item': '802.1q VLAN ID', 'value': ['Disabled']}, {'status': None, 'item': '802.1q VLAN Priority', 'value': ['0']}, {'status': None, 'item': 'RMCP+ Cipher Suites', 'value': ['0,1,2,3,6,7,8,11,12']}, {'status': None, 'item': 'Cipher Suite Priv Max', 'value': ['caaaXXaaaXXaaXX', 'X=Cipher Suite Unused', 'c=CALLBACK', 'u=USER', 'o=OPERATOR', 'a=ADMIN', 'O=OEM']}
    ]
    '''
    dataItem=[]
    for d in data.splitlines() :       
        tmp = []
        for i in d.replace(":","|",1).split("|"):
            tmp.append(" ".join(i.split())  )
        if(tmp[0]==""):
            dataItem[-1]["value"].append(tmp[1])
        else:
            dataItem.append({  "item":tmp[0], "value":[tmp[1]], "status":None  })
    return dataItem
 
def mcinfoParser(data):
    '''[
    {'status': None, 'item': 'Device ID', 'value': ['36']}, 
    {'status': None, 'item': 'Device Revision', 'value': ['1']}, 
    {'status': None, 'item': 'Firmware Revision', 'value': ['2.23']}, 
    {'status': None, 'item': 'IPMI Version', 'value': ['2.0']}, 
    {'status': None, 'item': 'Manufacturer ID', 'value': ['6569']}, 
    {'status': None, 'item': 'Manufacturer Name', 'value': ['Unknown (0x19A9)']}, 
    {'status': None, 'item': 'Product ID', 'value': ['54 (0x0036)']}, 
    {'status': None, 'item': 'Product Name', 'value': ['Unknown (0x36)']}, 
    {'status': None, 'item': 'Device Available', 'value': ['yes']}, 
    {'status': None, 'item': 'Provides Device SDRs', 'value': ['no']}, 
    {'status': None, 'item': 'Additional Device Support', 'value': ['', 'Sensor Device', 'SDR Repository Device', 'SEL Device', 'FRU Inventory Device', 'IPMB Event Receiver', 'IPMB Event Generator', 'Chassis Device']}, 
    {'status': None, 'item': 'Aux Firmware Rev Info', 'value': ['', '0x00', '0x00', '0x00', '0x00']}
    ]

    '''
    dataItem=[]
    for d in data.splitlines() :       
        tmp = []
        if(":" in d):
            for i in d.split(":"):
                tmp.append(" ".join(i.split())  )
            dataItem.append({  "item":tmp[0], "value":[tmp[1]], "status":None  })
        else:
            tmp.append(" ".join(d.split()))
            dataItem[-1]["value"].append(tmp[0])
        
    return dataItem
   
def powerParser(data):
    data = data.replace("\n","")
    if(data in "Chassis Power is on"):
        return [{"power":"on"}]
    if(data in "Chassis Power is off"):
        return [{"power":"off"}]
    return [{"power":"unknow"}]

def ipmiParser(data):
    result=""
    #print data.count(":"),data.count("|")
 
    if(data.count("|") > data.count(":") ):
        print ">> ipmitool sdr"
        result = sdrParser(data)
    else:
        if("Device" in data):
            print ">> ipmitool mc info"
            result = mcinfoParser(data)
        elif("IP" in data):
            print ">> ipmitool lan print"
            result = lanParser(data)
        elif("Power" in data):
            print ">> ipmitool power status"
            result = powerParser(data)
    return result 

def postData(data,url):
    print "URL : ",url
    print data # Note : json use "null" for None
    f = urllib2.urlopen(
            url  ,
            data    = urllib.urlencode(data)
            )
    print f.read()

def main():    
    
    
    # Get BMC IPMI DATA
    #ip = ipmiSettings.get("IP")
    url = 'http://nobearlabs.com/machine/apiIpmi/'
    
    for ip in ipmiSettings.get("IP"):
        result ={}
        result["BMC"] = [ip]
        for kkey,command in ipmiSettings.get("COMMAND").items(): # "sensor","network","machine"
            print "======= BMC :",ip," =================="
            print "*-*-*-*-*-*-*-*-*-*-*-*-*" 
            data = exeIpmiCommand(command,ip) 
            print "--------"
            print data
            print "--------"
            
            dataJson = ipmiParser(data)
            result[kkey] = dataJson
            print "dataJson : \n",dataJson
            print "*-*-*-*-*-*-*-*-*-*-*-*-*" 
            print "\n\n"
        print result
        postData(result,url)    
if __name__ == "__main__":
    main()
    


