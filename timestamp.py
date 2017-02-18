import datetime
import time

dt = datetime.datetime.now()

timestamp = dt.hour

nystart = 6
nyend = 18

if (nystart <= timestamp <=nyend):
    print ('New York store is open!')
else:
    print ('New York Store is closed')

ldstart = 1
ldend = 13

if (nystart <= timestamp <=nyend):
    print ('London store is open!')
else:
    print ('London Store is closed')

    


    
