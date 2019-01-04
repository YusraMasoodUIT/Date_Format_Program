def datemonth():
    date1 = None
    date2 = None
    list1 = []
    for count in range(10):
        date = input("Enter the date ")
        list1.append(date)

    print("\n\n")
    for d in list1:
        print("\n\n")
        print(d)
        letter = 0
        for lett in d:
            if lett.isalpha() == True:
               letter = letter + 1
        if letter > 0:
            print("Error, You have entered letters in your date "+d+", Please correct it.")
        elif letter == 0:
            a = d.split("-")
            length=len(a)
            if length != 3:
                print("Error, you have entered digits more than required. Please correct it ")
            else:
                x= a[0]
                y= a[1]
                z= a[2]
                lendate = len(x)
                lenmonth = len(y)
                lenyear = len(z)
                if lendate == 2 and lenmonth == 2 and lenyear == 2:
                    x= int(a[0])
                    y= int(a[1])
                    z= int(a[2])
                    if x > 00 and x < 32:
                        date1 = True
                    else:
                        date1 = False
                    if y > 00 and y < 13:
                        date2 = True
                    else:
                        date2 = False
        
                    if date1 == True and date2 == True:
                        print("Date "+d+ " is in correct format")
                    if date1 == True and date2 == False:
                        print("You have entered the wrong value of the month(mm) for date "+d+ ". Please correct it")
                    if date1 == False and date2 == True:
                        print("You have entered the wrong value of the day(dd) for date "+d+ ". Please correct it")
                elif lendate != 2 and lenmonth == 2 and lenyear == 2:
                    print("Error, There are more than 2 digits in day(dd)")
                elif lendate == 2 and lenmonth != 2 and lenyear == 2:
                    print("Error, There are more than 2 digits in month(mm)")
                elif lendate == 2 and lenmonth == 2 and lenyear != 2:
                    print("Error, There are more than 2 digits in year(yy)")
                else:
                    print("Error, The number of digits entered in the date "+d+ " is not according to the format dd-mm-yy")


def monthdate():
    date1 = None
    date2 = None
    list1 = []
    for count in range(10):
        date = input("Enter the date ")
        list1.append(date)

    print("\n\n")
    for d in list1:
        print("\n\n")
        print(d)
        letter = 0
        for lett in d:
            if lett.isalpha() == True:
               letter = letter + 1
        if letter > 0:
            print("Error, You have entered letters in your date "+d+", Please correct it.")
        elif letter == 0:
            a = d.split("-")
            length=len(a)
            if length != 3:
                print("Error, you have entered digits more than required. Please correct it ")
            else:
                x= a[0]
                y= a[1]
                z= a[2]
                lendate = len(x)
                lenmonth = len(y)
                lenyear = len(z)
                if lendate == 2 and lenmonth == 2 and lenyear == 2:
                    x= int(a[0])
                    y= int(a[1])
                    z= int(a[2])
                    if x > 00 and x < 13:
                        date1 = True
                    else:
                        date1 = False
                    if y > 00 and y < 32:
                        date2 = True
                    else:
                        date2 = False
        
                    if date1 == True and date2 == True:
                        print("Date "+d+ " is in correct format")
                    if date1 == True and date2 == False:
                        print("You have entered the wrong value of the day(dd) for date "+d+ ". Please correct it")
                    if date1 == False and date2 == True:
                        print("You have entered the wrong value of the month(mm) for date "+d+ ". Please correct it")
                elif lendate != 2 and lenmonth == 2 and lenyear == 2:
                    print("Error, There are more than 2 digits in dd(date)")
                elif lendate == 2 and lenmonth != 2 and lenyear == 2:
                    print("Error, There are more than 2 digits in mm(month)")
                elif lendate == 2 and lenmonth == 2 and lenyear != 2:
                    print("Error, There are more than 2 digits in yy(year)")
                else:
                    print("Error, The number of digits entered in the date "+d+ " is not according to the format dd-mm-yy")

                    
datefmt = input("Enter the date format , dd-mm-yy / mm-dd-yy ")
while datefmt != "dd-mm-yy" and datefmt != "mm-dd-yy" :
    print("Sorry you didn't entered the correct choice ,Please try again ")
    datefmt = input("Enter the date format , dd-mm-yy / mm-dd-yy ")

    if datefmt == "dd-mm-yy" or datefmt == "mm-dd-yy":
        break


if datefmt == "dd-mm-yy":
    print("\n")
    datemonth()
else:
    print("\n")
    monthdate()


input()
