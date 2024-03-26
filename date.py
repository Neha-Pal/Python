mydate = input('Enter a date(mm/dd/yyyy): ')
datelist = mydate.split('/')

month = int(datelist[0])
day = int(datelist[1])
year = int(datelist[2])

if month == 1:
    month = 'January'
elif month == 2:
    month = 'February'
elif month == 3:
    month = 'March'
elif month == 4:
    month = 'April'
elif month == 5:
    month = 'May'
elif month == 6:
    month = 'June'
elif month == 7:
    month = 'July'
elif month == 8:
    month = 'August'
elif month == 9:
    month = 'September'
elif month == 10:
    month = 'October'
elif month == 11:
    month = 'November'
elif month == 12:
    month = 'December'
    
newdate = month + ' ' + str(day )+ ',' + str(year )
print(newdate)