import time;

ticktock = time.time();
print("Number of ticks:", ticktock)

currentTime = time.localtime(time.time())
print("current time: ", currentTime)
print("Current year: ", currentTime.tm_year)
print("Current month: ", currentTime.tm_mon)
print("Current day: ", currentTime.tm_mday)
print("Current hour: ", currentTime.tm_hour )
print("Current minutes: ", currentTime.tm_min )
print("Current second(s): ", currentTime.tm_sec )