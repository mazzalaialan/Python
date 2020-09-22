import os
import datetime
import time

flag_entro = False
now = datetime.datetime.now()
my_time_string = "09:00:00"

while True:
    my_datetime = datetime.datetime.strptime(my_time_string, "%H:%M:%S")

    # I am supposing that the date must be the same as now
    my_datetime = now.replace(hour=my_datetime.time().hour, minute=my_datetime.time().minute, second=my_datetime.time().second, microsecond=0)

    if (now == my_datetime):
        os.system("start \"\" https://us04web.zoom.us/j/78722029006?pwd=MTY3WTJasfasWEJjTHExVlJiQT09") #Windows
        #os.system("xdg-open \"\" https://us04web.zoom.us/j/78722029006?pwd=MTY3WTJasfasWEJjTHExVlJiQT09") #Linux
        break
    else:
        print('Todavia falta: ' + now.strftime("%H:%M:%S"))
        time.sleep(60)
        continue