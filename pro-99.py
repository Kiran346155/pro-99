import os
import shutil
source= input("enter the source folder")
destination= input("enter the destination folder")
for route,folders,files in os.walk(source):
    for file in files:
        shutil.copy(route+"/"+file,destination+"/"+file)
        os.stat(route+"/"+file).st_ctime