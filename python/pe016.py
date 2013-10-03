'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?

Answer = 1366
'''

import time

	
if __name__ == "__main__":
	start = time.time()
	result = sum(int(digit) for digit in str(1<<1000))
	elapsed = (time.time() - start)
	 
	print "result %s returned in %s seconds." % (result,elapsed)