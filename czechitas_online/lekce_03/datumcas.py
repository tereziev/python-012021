from datetime import datetime, timedelta

datetime.now()
datetime(2020, 11, 21, 20, 26, 26, 472567)

apolloStart = datetime(1969, 7, 16, 14, 32)
print(apolloStart)

apolloStart.strftime("%m/ %d/ %Y, %H:%H")
#print(f"{apolloStart.month}/{apolloStart.day}/{apolloStart.year}")

print(apolloStart)

apolloPristani = datetime.strptime("21. 7. 1969, 18:54", "%d. %m. %Y, %H:%M")
delkaMise = apolloPristani - apolloStart
print(delkaMise)

solarOrbiterStart = datetime(2020, 2, 10, 5, 3)
print(solarOrbiterStart.isoweekday())
