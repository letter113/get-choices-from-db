#!/app/python/2.4.1/bin/python

#import optparse
import sys
#import re
#import os
#import string
#import time
#import threading
#import Queue

sys.path.append("/vobs/erbs/int/sst/lib")
#sys.path.append("/usr/atria/bin")
from lmint.dbhandler import DbHandler

collectionrev="LteDc_16-P1A964"
#collectionrev="LteDc_16-P1A1106"

testid, ongoing, passed, failed, skipped, teststarted, uprev = None, None, None, None, None, None, None

ipadhandler = DbHandler(host="mysql-lte.rnd.ki.sw.ericsson.se",
                        user="ltedailyatest_ro",
                        passwd="guitar",
                        db="ltedailyatest")
    
#q = "SELECT rev.name, rev.id, exec.ongoing, exec.passed, exec.failed, exec.skipped, up.name\
#     FROM LmCollectionRevs AS rev,\
#     LmTestExecutions AS exec,\
#     Ups as up\
#     WHERE rev.id = exec.lmcollectionrev_id\
#     AND exec.up_id = up.id"

#q = "SELECT rev.name, rev.id, exec.ongoing, exec.passed, exec.failed, exec.skipped, up.name\
#     FROM LmCollectionRevs AS rev,\
#     LmTestExecutions AS exec,\
#     Ups as up\
#     WHERE rev.id = exec.lmcollectionrev_id\
#     AND exec.up_id = up.id"

q = "SELECT rev.name, rev.id, exec.ongoing, exec.passed, exec.failed, exec.skipped, up.name\
     FROM LmCollectionRevs AS rev,\
     LmTestExecutions AS exec,\
     Ups as up\
     WHERE rev.name = \"%s\"\
     AND rev.id = exec.lmcollectionrev_id\
     AND exec.up_id = up.id" % collectionrev
     
#q = "SELECT rev.name, rev.id, exec.ongoing, exec.passed, exec.failed, exec.skipped, up.name\
#     FROM LmCollectionRevs AS rev,\
#     LmTestExecutions AS exec,\
#     Ups as up\
#     WHERE rev.name = \"%s\"\
#     AND rev.id = exec.lmcollectionrev_id" % collectionrev
     
cursor = ipadhandler.query(q)
foo = cursor.fetchall()

for record in foo:
   revname = record[0]
   testid  = record[1]
   ongoing = record[2]
   passed  = record[3]
   failed  = record[4]
   skipped = record[5]
   uprev   = record[6]
            
print ("Query=" + q)
print ("NrOfRow=" + str(cursor.rowcount) + " Result=" + str(foo))

if ongoing == 0:
   print ("Test has completed")
elif ongoing == 1:
   print ("Test has started")
else:
   print ("Unknown")
   
cursor.close()
ipadhandler.close()
        
sys.exit(0)
