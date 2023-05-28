for i in range(41):

        if i % 35 == 0 :
            print ("{} is divided by 5 and 7".format(i))
        elif i % 7 == 0:
            print ("{} is divided by 7".format(i))
        elif i % 5 == 0:
            print ("{} is divided by 5".format(i))
        elif i == 13:
            pass
        else:
            print("{} is not important".format(i))

print("")

i = 1
while i < 41:
    if i % 35 == 0:
        print("{} is divided by 5 and 7".format(i))
    elif i % 7 == 0:
        print("{} is divided by 7".format(i))
    elif i % 5 == 0:
        print("{} is divided by 5".format(i))
    elif i == 13:
        pass
    else:
        print("{} is not important".format(i))
    i+=1