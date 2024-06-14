# Begins recording time from the epoch that begins at 00:00:00,1st Jan 1970
import time
print(time.time())
print(time.ctime())

print(time.localtime())
a=time.localtime()
b=time.mktime(a)
print(b)
c=time.asctime(a)
print(c)
help(time.strftime)
x=time.strftime("%m/%d/%Y")
print(x)
y="08 August 2019"
s=time.strptime(y,"%d %B %Y")
print(s)

import datetime
