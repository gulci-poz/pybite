# coding: utf-8

import datetime
# wykonuje wszystko, ale zostawia tylko to, co jest potrzebne
# może też się wykonać inny kod z pliku, np. wywołania
#from datetime import datetime as dt

print(datetime.date)
print(datetime.time)
print(datetime.datetime.now())

# definiujemy obiekt na podstawie podanego czasu
wtedy = datetime.datetime(2015, 10, 27, 10, 15, 15)
teraz = datetime.datetime.now()

print(wtedy)

# timedelta da nam różnice
# na takim obiekcie możemy dalej operować
delta = (teraz - wtedy).seconds

print(delta)
print(type(datetime.datetime))
