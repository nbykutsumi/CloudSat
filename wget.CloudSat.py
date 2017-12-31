#import subprocess
from ftplib import FTP
from datetime import datetime, timedelta
import myfunc.util as util
import calendar
import os
hostname = "ftp.cloudsat.cira.colostate.edu"
prdName = "2B-CLDCLASS.P_R04"
#prdName = "2B-GEOPROF.P_R04"
myid    = "nbyk.utsumi"
mypass  = "suimongaku"

#iYM    = [2014,3]
#eYM    = [2015,7]
#iYM    = [2014,11]
#eYM    = [2015,3]

iYM    = [2008,1]
eYM    = [2009,12]


lYM    = util.ret_lYM(iYM, eYM)
#lYM = [YM for YM in lYM if YM[1] not in [11,12,1,2,3]]
#lYM = [YM for YM in lYM if YM[1] not in [11,12,1,2,3]+[5,7,9]]
#lYM = [YM for YM in lYM if YM[1] not in [11,12,1,2,3]+[4,6,8,10]]

ibaseDir = "/%s"%(prdName)
obaseDir = "/media/disk2/data/CloudSat/%s"%(prdName)

ftp = FTP(hostname)
ftp.login(myid, mypass)
#-----------------------------------------
for [Year,Mon] in lYM:
  iDay = 1
  eDay = calendar.monthrange(Year,Mon)[1]
  iDTime = datetime(Year,Mon,iDay,0)
  eDTime = datetime(Year,Mon,eDay,0)
  iDOY   = iDTime.timetuple().tm_yday   # Day Of Year
  eDOY   = eDTime.timetuple().tm_yday
  for DOY in range(iDOY, eDOY+1):
    iDir  = ibaseDir + "/%04d/%03d"%(Year,DOY)
    oDir  = obaseDir + "/%04d/%03d"%(Year,DOY)
    util.mk_dir(oDir)
    lPath = ftp.nlst(iDir)
    for sPath in lPath:
      oPath = oDir + "/" + sPath.split("/")[-1]
      ftp.retrbinary("RETR %s"%(sPath), open(oPath, "wb").write)
      print oPath

ftp.close() 
#
