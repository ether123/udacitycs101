#Given your birthday and the current date, calculate your age in days. Compensate for leap days. 
#Assume that the birthday and current date are correct dates (and no time travel). 
#Simply put, if you were born 1 Jan 2012 and todays date is 2 Jan 2012 you are 1 day old.

def LeapYear(year):
   if(year % 100 != 0):
    return(year % 4 == 0)
   else:
    return(year % 400 == 0)

def daysInMonth(year, month):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    if LeapYear(year):
        months[1] = 29
    return months[month-1]

def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def dateIsAfter(year1, month1, day1, year2, month2, day2):
    if year1 > year2:
        return True
    if year1 == year2:
        if month1 > month2:
            return True
        if month1 == month2:
            return day1 > day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert not dateIsAfter(year1, month1, day1, year2, month2, day2)
    days = 0
    while dateIsAfter(year2, month2, day2, year1, month1, day1):
        days += 1
        (year1, month1, day1) = nextDay(year1, month1, day1)
    return days

def test():
    assert daysBetweenDates(2013,1,1,2013,1,1) == 0
    assert daysBetweenDates(2-13,1,1,2013,1,2) == 1
    assert nextDay(2013,1,1) == (2013,1,2) 
    assert nextDay(2013,4,30) == (2013,5,1)
    print "Tests finished."

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"
