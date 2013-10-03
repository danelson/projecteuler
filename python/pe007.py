'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.

What is the 10001st prime number?

Answer = 104743
'''

import time
import math

def find_n_primes(n):
	primes = [2,3]
	current = 5
	flag = True
	
	while len(primes) < n:
		for i in range(2,int(math.sqrt(current)) + 1):
			if (current%i) == 0:
				break
			if i == int(math.sqrt(current)):
				primes.append(current)
				print current
		current += 2
	return primes
	
if __name__ == "__main__":
	start = time.time()
	result = find_n_primes(10001)[-1]
	elapsed = (time.time() - start)
	print "result %s returned in %s seconds." % (result,elapsed)