#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
#see that the 6th prime is 13.

#What is the 10001st prime number?

#Answer 104743

import math
	
def find_primes(n):
	primes = [2]
	current = 3
	flag = True
	
	while True:
		if len(primes) == n:
			return primes
			
		end = int(math.sqrt(current)) + 1
		for i in range(2,end):
			if (current%i) == 0:
				flag = False
				break
		
		if flag:
			primes.append(current)
		flag = True
		current += 1
			

if __name__ == "__main__":
	
	print find_primes(10001)[-1]