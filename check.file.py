import socket, os, sys
from datetime import datetime, timedelta
import myfunc.util as util
import glob

myhost = socket.gethostname()

prdName = "2B-CLDCLASS.P_R04"
if myhost == "mizu":
  obaseDir = "/home/utsumi/mnt/wellshare/CloudSat/%s"%(prdName)
elif myhost == "well":
  obaseDir = "/media/disk2/data/CloudSat/%s"%(prdName)

iDTime = datetime(2008,1,1)
eDTime = datetime(2008,12,31)
dDTime = timedelta(days=1)
lDTime = util.ret_lDTime(iDTime, eDTime, dDTime)

lastID = -9999
lastDTime= datetime(1900,1,1)
lastDOY  = -9999
lastsDATE = "-9999"
for DTime in lDTime:
    Year = DTime.year
    Mon  = DTime.month
    Day  = DTime.day
    DTime0= datetime(Year,1,1)
    DOY   = (DTime - DTime0).days +1
    sDATE = "%04d-%02d-%02d (%03d)"%(Year,Mon,Day,DOY)

    srcDir= obaseDir + "/%04d/%03d"%(Year,DOY)
    lsrcPath = glob.glob(srcDir + "/*.hdf")
    lsrcPath = sorted(lsrcPath)
    for srcPath in lsrcPath:
        fileName = srcPath.split("/")[-1]
        ID       = int(fileName.split("_")[1])
        if ID != lastID+1:
            print "No file ID=",lastID+1," -- ",ID-1, "(",lastsDATE," -- ",sDATE,")"
        lastID = ID
        lastDTime = DTime
        lastDOYH  = DOY
        lastsDATE = sDATE
        
