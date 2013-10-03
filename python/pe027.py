'''
Euler published the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered, which
produces 80 primes for the consecutive values n = 0 to 79. The product of the
coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n^2 + an + b, where |a|  1000 and |b|  1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.

Answer = -59231
'''

import time
import math

def isPrime(n):
	if n < 2:
		return False
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False

	return True

def quadratic(a,b):
	n = 0
	while True:
		if not isPrime(n**2 + a*n + b):
			break
		n += 1
	return n
	
def main():
	primesUnder1000 = [i for i in range(2,1000) if isPrime(i)]
	
	consecutivePrimes = 0
	a,b = 0,0
	for i in range(-1000,1000):
		for j in primesUnder1000:
			if quadratic(i,j) > consecutivePrimes:
				a,b = i,j
			consecutivePrimes = max(quadratic(i,j),consecutivePrimes)
			
	return a*b
				

if __name__ == "__main__":
	start = time.time()
	result = main()
	elapsed = (time.time() - start)
	print "result %s returned in %s seconds." % (result,elapsed)
	
	
	