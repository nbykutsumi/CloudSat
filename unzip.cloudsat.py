import os,sys
import glob
import subprocess
import calendar
import myfunc.util as util
from   datetime    import datetime, timedelta

#rootDir = "/home/utsumi/mnt/well.share/CloudSat/2B-CLDCLASS.P_R04/2014"
#rootDir = "/home/utsumi/mnt/well.share/CloudSat"
rootDir = "/media/disk2/share/CloudSat"
varName = "2B-CLDCLASS.P_R04"

iYM = [2008,1]
eYM = [2008,12]
lYM = util.ret_lYM(iYM, eYM)
#lYM = [YM for YM in lYM if YM[1] not in [11,12,1,2,3] + [5,7,9]]
#lYM = [YM for YM in lYM if YM[1] not in [11,12,1,2,3] + [4,6,8,10]]

for Year,Mon in lYM:
  iDay   = 1
  eDay   = calendar.monthrange(Year,Mon)[1]
  #eDay   = 1
  iDTime = datetime(Year,Mon,iDay,0)
  eDTime = datetime(Year,Mon,eDay,0)
  dDTime = timedelta(days=1)
  lDTime = util.ret_lDTime(iDTime, eDTime, dDTime)
  for DTime in lDTime:
    DOY = DTime.timetuple().tm_yday
    srcDir = os.path.join(rootDir, varName, "%04d"%Year, "%03d"%DOY)
    if not os.path.exists(srcDir):
       print "No directory"
       print srcDir
       sys.exit()

    lsrcPath = glob.glob(srcDir+"/*.zip")

    for srcPath in lsrcPath:
      outPath = srcPath[:-4]
      cmd    = ["unzip", "-u",srcPath,"-d",srcDir]
      subprocess.call(cmd)
      os.remove(srcPath)
