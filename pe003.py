'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Answer = 6857
'''

import time

def prime_factors(n):
	'''
	Returns all the prime factors of a positive integer
	'''
	factors = []
	dividend = 2
	while (n > 1):
		while (n%dividend == 0):
			factors.append(dividend)
			n /= dividend

		dividend = dividend + 1

		if (dividend**2 > n):
			if (n>1):
				factors.append(n)
			break

	return factors	


if __name__ == "__main__":
	start = time.time()
	result = prime_factors(600851475143)[-1]
	elapsed = (time.time() - start)
	print "result %s returned in %s seconds." % (result,elapsed)