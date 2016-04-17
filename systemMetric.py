import json
import urllib

url = 'http://localhost:9200/topbeat-*/_search?pretty'

print "Retrieving " + url

fileData = urllib.urlopen(url).read()

print "Retrieved " + str(len(fileData)) + " Characters"

dObj = json.loads(fileData)

infoObj = dObj["hits"]["hits"]

infoObj1 = infoObj[0]["_source"]
infoObj2 = infoObj[1]["_source"]

cpuInfo = infoObj1["cpu"]
memInfo = infoObj1["mem"]

fileSysinfo = infoObj2["fs"]

print "\n\n                    CPU usage "
print "========================================================"
print "User usage:%d" % (cpuInfo["user"])
print "User usage in percentage:%.2f%%" % (cpuInfo["user_p"]*100)
print "System usage:%d" % (cpuInfo["system"])
print "System usage in percentage:%.2f%%" % (cpuInfo["system_p"]*100)

print "\n\n                    Memory usage "
print "========================================================"
print "Total memory:%d" % (memInfo["total"])
print "Used Memory:%d" % (memInfo["used"])
print "Used memory in percentage:%.2f%%" % (memInfo["used_p"]*100)
print "Free memory:%d" % (memInfo["free"])

print "\n\n                    Disk usage "
print "========================================================"
print "Total storage:%d" % (fileSysinfo["total"])
print "Used storage:%d" % (fileSysinfo["used"])
print "Used storage in percentage:%.2f%%" % (fileSysinfo["used_p"]*100)
print "Free storage:%d" % (fileSysinfo["free"])

print "\n\n"