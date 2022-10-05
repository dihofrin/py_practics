import math
from datetime import date, datetime, timedelta

pattern = '%d.%m.%Y %H:%M'
dt = datetime.strptime(input(), pattern)
course = datetime(2022, 11, 8, 12)
if dt > course:
    print('Курс уже вышел!')
else:
    days = math.floor((course-dt).total_seconds()/3600/24)
    if days < 1:
        hours = (course-dt).seconds/3600
    else:
        hours = math.floor((course-dt).seconds*60*60)
    print(days, hours)