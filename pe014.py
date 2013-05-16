'''
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Answer = 837799
'''

import time


def collatz_slow(n):
	count = 1
	size = 0
	value = 0
	for i in range(n):
		current = i
		while current > 1:
			if current % 2 == 0:
				current = current/2
			else:
				current = current*3 + 1
			count += 1
		
		if count > size:
			size = count
			value = i
			print value, size
		count = 1
	return value,size

def collatz_fast(n, cache):
    if not n in cache:
        if n%2 == 0:
            cache[n] = collatz(n/2, cache) + 1
        else:
            cache[n] = collatz((3*n + 1)/2, cache) + 2
    return cache[n]

def main():
	cache = {1:1}
	for i in range(1000000,0,-1):
		collatz_fast(i, cache)
		
	return cache.keys()[cache.values().index(max(cache.values()))] 
 


if __name__ == "__main__":
	start = time.time()
	result = main()
	elapsed = (time.time() - start)
	
	print "result %s returned in %s seconds." % (result,elapsed)
