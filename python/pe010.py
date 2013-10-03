#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

#Answer = 142913828922

'''
def eratosthenes(n):
	multiples = []
	primes = 0
	for i in range(2, n,2):
		if i not in multiples:
			primes += i
			for j in range(i**2, n, i):
				multiples.append(j)
	
	return primes
'''

def eratosthenes(n):
	'''Set lookup is much faster than list lookup'''
	sum = 0
	multiples = set()
	for i in range(2, n+1):
		if i not in multiples:
			sum += i
			multiples.update(range(i*i, n+1, i))
	return sum

	
if __name__ == "__main__":
	start = time.time()
	result = eratosthenes(2000000)
	elapsed = (time.time() - start)
	print "result %s returned in %s seconds." % (result,elapsed)