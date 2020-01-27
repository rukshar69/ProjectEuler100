import datetime

count = 0
for year in range(1901, 2001):
    for month in range(1,13):


        thisXMas    = datetime.date(year,month,1)

        thisXMasDay = thisXMas.weekday()

        if thisXMasDay == 6: count+=1

print(count)
