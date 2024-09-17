import time

c = time.time()
d = c//1_704_326_400
print (d)

days = 19726
hours = 473424
seconds = 1_704_326_400
seconds_time = seconds % 60 
minutes = seconds//60
minutes_time = minutes % 60
hour = minutes // 60
hour_time = hour % 60 

hour = minutes//60

day = hour // 24
day_time = hour % 24

print (seconds_time)
print (minutes_time)
print (hour_time)
print (day_time)