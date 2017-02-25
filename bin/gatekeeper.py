import os
import time
import datetime

app_path = '/srv/FamilyPhoto/'
dropoff_path = app_path + 'dropoff/'
logpath = app_path + 'log/gatekeeper/'
store_path = app_path + 'store/'

if(len(os.listdir(dropoff_path))) > 0:
    move_cnt = 0
    warn_cnt = 0
    millis = int(round(time.time() * 1000))
    today = str(datetime.date.today())
    logname = 'gatekeeper_' + today + '_' +  str(millis) + '.log'
    logfile = open(logpath + logname, 'w') 
    logfile.write(" %sbin/gatekeeper.py           Gatekeeper Processing Log      Date:  %s\n\n"%(app_path,today)) 

    for item in os.listdir(dropoff_path):
        if os.path.isfile(dropoff_path + item):
	    os.rename(dropoff_path + item, store_path + item)
	    logfile.write("Moved %s%s to %s%s"%(dropoff_path,item,store_path,item))
	    move_cnt += 1
        else:
            logfile.write("WARNING: Found a directory '%s' in dropoff items. Please breakdown the directory into files to be added to the application\n"%(item))
            warn_cnt += 1
    logfile.write("\n\nMoved %d items from dropoff to store."%(move_cnt))
    logfile.write("\n\nThere were %d issues found."%(warn_cnt))

    logfile.close()
