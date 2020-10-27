import time
now = time.gmtime()

print(str(now[2])+'/'+str((now[1]))+'/'+str(now[0])+'|'+str(now[3]+7)+':'+str(now[4])+':'+str(now[5])+"| ( UTC+7.00)")