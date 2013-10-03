'''
You are given the following information, but you may prefer to do some
research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?

Answer = 171
'''

import calendar
import time

def sundays(start, end):
	days = 0
	for year in range(start,end+1):
		for month in range(1,13):
			if calendar.monthrange(year,month)[0] == 6:
				days += 1
	return days

if __name__ == "__main__":
	start = time.time()
	result = sundays(1901, 2000)
	elapsed = (time.time() - start)
	print "result %s returned in %s seconds." % (result,elapsed)