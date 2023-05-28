import os
import datetime
import random


def find_pdf_size(top):
    size = 0
    for root, dirs, files in os.walk(top):
        for name in files:
            if name.endswith(".pdf"):
                fullpath = os.path.join(root, name)
                print(fullpath)
                size += os.path.getsize(fullpath)
    return size


''' exercise 5.2'''

def print_working_days1(date1, date2):
    d1 = datetime.date.fromisoformat(date1)
    d2 = datetime.date.fromisoformat(date2)
    delta = datetime.timedelta(days = 1)
    day = d1
    while day < d2:
        if day.weekday() <5:
            print (day.isoformat())
        day = day + delta

def print_working_days2(date1, date2):
    d1 = datetime.date.fromisoformat(date1)
    d2 = datetime.date.fromisoformat(date2)
    day_generator = (d1 + datetime.timedelta(i) for i in range((d2-d1).days))
    for day in day_generator:
        if day.weekday() < 5:
            print(day.isoformat())


'''exercise 5.3'''

def random_walk(start=0):
    pos = start
    while True:
        yield pos += random.choice([-1,1])


for pos in random_walk():
    print(pos, end = ' ')
    if abs(pos) == 5:
        break

results = []
for iteration in range(10):
    rw = random_walk()
    for step in range(100):
        '''nie dokończone'''

