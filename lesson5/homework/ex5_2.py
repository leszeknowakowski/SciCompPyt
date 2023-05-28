import datetime

date1 = "2023-03-20"
date2 = "2023-04-01"
def date_convert(date):
    date_list = date.split("-")
    date_list_int=[]
    for i in range(len(date_list)):
         date_int = int(date_list[i])
         date_list_int.append(date_int)
    return datetime.date(date_list_int[0],date_list_int[1],date_list_int[2])

def weekdays(date1, date2):
   date1_day = date_convert(date1)
   date2_day = date_convert(date2)
   datedelta = date2_day - date1_day
   if date1_day > date2_day:
       print ("second date must be later than the first! ")
   else:
      actual_day = date_convert(date1)
      print("working days from {} to {}:".format(date1, date2))
      for i in range(datedelta.days):
        if actual_day.isoweekday() == 1:
            print("{} : Monday".format(actual_day))
        elif actual_day.isoweekday() == 2:
            print("{} : Tuesday".format(actual_day))
        elif actual_day.isoweekday() == 3:
            print("{} : Wednesday".format(actual_day))
        elif actual_day.isoweekday() == 4:
            print("{} : Thursday".format(actual_day))
        elif actual_day.isoweekday() == 5:
            print("{} : Friday".format(actual_day))
        else:
            pass
        actual_day += datetime.timedelta(1)


weekdays(date1,date2)

