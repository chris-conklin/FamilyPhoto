import os
import time
import datetime

#app_path = '/srv/FamilyPhoto/'
#dropoff_path = app_path + 'dropoff/'
app_path = '/Users/cconklin/src/FamilyPhoto/'
dropoff_path = app_path + 'dropoff/'
logpath = app_path + 'log/'


millis = int(round(time.time() * 1000))
logname = 'gatekeeper_' + str(datetime.date.today()) + '_' +  str(millis) + '.log'
logfile = open(logpath + logname, 'w') 


for item in os.listdir(dropoff_path):
    if os.path.isfile(dropoff_path + item):
        logfile.write("Found a file " + item)
    else:
        logfile.write("Found a directory " + item)


