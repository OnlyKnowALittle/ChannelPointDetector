import datetime

time = datetime.datetime.now().strftime('%I:%M %p')
hour = int(datetime.datetime.now().strftime('%I'))

print("This is the hour")
print(hour)
print(time[0:2])

print('the current time is ' + time)
if hour>1:
    print("wow late night bitch?")