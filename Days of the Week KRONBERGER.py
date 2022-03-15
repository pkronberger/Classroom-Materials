monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
dayList = [3,0,3,2,3,2,3,3,2,3,2,3]
dayOfWeekList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Monday"]


def leftOverDays(month, day, year):
	daysLeft = 2;
	if (month=="January"):
		daysLeft = -1;
	return daysLeft

def dayOfTheWeek(month, day, year):
	totalDays = leftOverDays(month, day, year)
	totalDays += day % 7
	totalDays += year % 7 -1
	totalDays += leapYear(month, year) % 7
	totalDays += monthsBetween(month) % 7
	return dayOfWeekList[totalDays % 7]

def monthsBetween(month):
	sum = 0
	if (month != "January"):
		stop = monthList.index(month)
		for m in range (2,stop):
			sum += dayList[m]
	return sum

def leapYear(month, year):
	countLeap = 0;
	if (month != "January"):
		year+=1
	for y in range(1, year):
		if (y%4==0 and (y%100!=0 or y%400==0)):
			countLeap+=1
	return countLeap

def findDay():
    myMonth = input("Enter the month: ")
    try:
        monthNum = monthList.index(myMonth)
    except ValueError:
        input("Please enter a month from January through December. ")
        findDay()
    myDay = int(input("Enter the day: "))
    while (myDay < 1 or myDay > dayList[monthNum] + 28):
        input("Please enter a correct date for the month of " + myMonth + ". ")
        myDay = int(input("Enter the day: "))
    myYear = int(input("Enter the year: "))
    print(myMonth + " " + str(myDay) + ", " + str(myYear) + " : " + dayOfTheWeek(myMonth,myDay,myYear))
    another = input("Would you like to continue? y/n :")

another = "y"

while (another == "y" or another == "Y" or another == "yes" or another == "Yes"):
    findDay()
