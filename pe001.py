'''
Add all the natural numbers below one thousand that are multiples of 3 or 5.

Answer: 233168
'''

import time

def multiples3and5(x):
	value = 0
	for i in range(x):
		if i % 3 == 0 or i % 5 == 0:
			value += i
	return value

if __name__ == "__main__":
	start = time.time()
	result = multiples3and5(1000)
	elapsed = (time.time() - start)
	print "result %s returned in %s seconds." % (result,elapsed)