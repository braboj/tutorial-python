##################################################################################################

import datetime as datetime

##################################################################################################
start = datetime.date(2021, 9, 6)
endtime = datetime.date(2021, 9, 6)

daygenerator = (endtime + datetime.timedelta(x) for x in range((endtime - start).days))
duetime = sum(1 for day in daygenerator if day.weekday() < 5)
print("Duetime {0}".format(duetime))

##################################################################################################

start = datetime.date(2021, 9, 6)
endtime = datetime.date.today()

daygenerator = (endtime + datetime.timedelta(x + 1) for x in range((endtime - start).days))
daysnow = sum(1 for day in daygenerator if day.weekday() < 5)
print("Days now {0}".format(daysnow))

##################################################################################################

print("Delay {0}".format(daysnow - (duetime + 15)))
