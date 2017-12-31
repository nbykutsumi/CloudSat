#import subprocess
from ftplib import FTP
from datetime import datetime, timedelta
import myfunc.util as util
import calendar
import os
import socket

hostname = "ftp.cloudsat.cira.colostate.edu"
prdName = "2B-CLDCLASS.P_R04"
#prdName = "2B-GEOPROF.P_R04"
myid    = "nbyk.utsumi"
mypass  = "suimongaku"


Year  = 2008
DOY   = 176
lID   = ["11483"]  # list of strings, not numbers

ibaseDir = "/%s"%(prdName)

myhost= socket.gethostname()
if myhost == "mizu":
  obaseDir = "/home/utsumi/mnt/wellshare/CloudSat/%s"%(prdName)
elif myhost == "well":
  obaseDir = "/media/disk2/data/CloudSat/%s"%(prdName)

ftp = FTP(hostname)
ftp.login(myid, mypass)
#-----------------------------------------
iDir  = ibaseDir + "/%04d/%03d"%(Year,DOY)
oDir  = obaseDir + "/%04d/%03d"%(Year,DOY)
util.mk_dir(oDir)
lPath = ftp.nlst(iDir)
for sPath in lPath:
  if len(lID) >0:
    sName= sPath.split("/")[-1]
    sID = sName.split("_")[1]
    if not sID in lID:
      print "Skip sID",sID
      continue
  oPath = oDir + "/" + sPath.split("/")[-1]
  ftp.retrbinary("RETR %s"%(sPath), open(oPath, "wb").write)
  print oPath

ftp.close() 
#
