import sys
import os
sh,sm=map(int,input().split())
dh,dm=map(int,input().split())

mm=sm+dm
hh=dh+sh
if(mm>59):
    hh=hh+int(mm/60)
    mm=int(mm%60)
if(hh>23):
    hh=int(hh%24)
#print(f"{hh:02d}" , f"{mm:02d }")
print(f"{hh:02d}", f"{mm:02d}")


