'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.

Answer = 21124
'''

import time


a = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]	# 0-19
b = [0,3,6,6,5,5,5,7,6,6]						# 10-90
c = 7											# 100
d = 8											# 1000


def sum_number_words(n):
	sum = 0
	for i in range(1,n):
		singles = i % 10
		tens = ((i % 100) - singles) / 10
		hundreds = ((i % 1000) - (tens*10) - singles) / 100
		
		if hundreds != 0:
			sum += a[hundreds] + c
			if tens != 0 or singles != 0:
				sum += 3
		if tens < 2:
			sum += a[tens*10+singles]
		else:
			sum += b[tens] + a[singles]
	
	sum += a[1] + d
	
	return sum
	
	
if __name__ == "__main__":
	start = time.time()
	result = sum_number_words(1000)
	elapsed = time.time() - start
	 
	print "%s found in %s seconds" % (result,elapsed)
		
		